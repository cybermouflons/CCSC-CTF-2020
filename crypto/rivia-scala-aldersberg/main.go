package main

import (
	"crypto/rand"
	"crypto/rsa"
	"encoding/hex"
	"fmt"
	"log"
	"math/big"
	mrand "math/rand"
	"net/http"
	"os"
	"text/template"
	"time"
)

/**
 * It is known there's treasure to be found between these 3 cities.
 */

var (
	port   = os.Getenv("CHALLENGE_PORT")
	flag   = os.Getenv("CHALLENGE_FLAG")
	logger = log.New(os.Stdout, "rivia-scala-aldersberg ", log.LstdFlags|log.Lshortfile)
)

// known factors in FactorDB
var knownFactors = []struct {
	p string
	q string
}{
	{
		p: "10059846168991443748286174859998005203299218822300999074514569188399315767558578427928732601273716692930765241273483388156557723300537590558169228894448359",
		q: "10601708587985313527067096495285541729365319188853415872832620975937484894946123327211001190351388846755364442368059831654741268267144328234312020393641547",
	},
	{
		p: "12819377845872787893236203998845763971359596020385438780666074008262006784691882378804485427182995122461611922518784211933209956012220476177158758536807939",
		q: "12226571580407151523926535654202327573133090215360287197617380583119325117965913083300387430080824145266313801077997908107836230625664979697341720498438161",
	},
	{
		p: "10107514651958314528951707395019036418878372470409896075651690153261083666801012617703958722850283846556874216048812073138773483899635428475103056587166399",
		q: "10248759846334369677323295441463585492691302074943653122143873213409990919110065565855353350986240700434880929482968926130067581841427358232479662933277209",
	},
	{
		p: "12230765293952642931581961851451080327112102115807496709860524977835350247071432853967841570890056736634363874181799398736269505357500614145311301456304017",
		q: "12960393916729742734851257435385726293059680413603842466851265766285654434277905059486326305487678782369450262739219063815865175898742879557338389655779667",
	},
	{
		p: "10808528790338635448074911260520464697043165620918902138051089263681833900862904596233253745421300173209922418205851010534917072361472207921219746839165747",
		q: "10314617812885196292347159814344825473839620295333696999303253294753981945957969786381550083264475204829877317099209434837583121030780117240260192515564349",
	},
}

func rsaGenerate() (*rsa.PrivateKey, error) {
	prvKey := &rsa.PrivateKey{}
	var big1 = big.NewInt(1)
	var big3 = big.NewInt(3)

	for {
		var err error
		var p *big.Int
		var q *big.Int

		// 1 in 5 chance to get a factorized N in FactorDB
		bias := mrand.Intn(5)
		useKnownFactors := bias < 1
		if useKnownFactors {
			idx := mrand.Intn(len(knownFactors))
			p, _ = new(big.Int).SetString(knownFactors[idx].p, 10)
			q, _ = new(big.Int).SetString(knownFactors[idx].q, 10)
		} else {
			p, err = rand.Prime(rand.Reader, 512)
			q, err = rand.Prime(rand.Reader, 512)
		}
		if err != nil {
			return nil, err
		}

		pMinusOne := new(big.Int).Sub(p, big1)
		qMinusOne := new(big.Int).Sub(q, big1)
		et := new(big.Int).Mul(pMinusOne, qMinusOne)

		prvKey.Primes = []*big.Int{p, q}
		prvKey.E = 3
		prvKey.N = new(big.Int).Mul(p, q)
		prvKey.D = new(big.Int).ModInverse(big3, et)

		// (p-1)*(q-1) is not a relative prime with E, D will be nil
		// if D is 1, our ciphertext will be the same as the plaintext
		if prvKey.D != nil && prvKey.D.Cmp(big1) > 0 {
			if useKnownFactors {
				logger.Println("used known factors")
			}
			break
		}
	}

	return prvKey, nil
}

func rsaEncrypt(m []byte, key *rsa.PublicKey) ([]byte, error) {
	mInt := new(big.Int).SetBytes(m)
	if mInt.Cmp(key.N) >= 0 {
		return nil, fmt.Errorf("m is bigger than N")
	}
	return mInt.Exp(mInt, big.NewInt(int64(key.E)), key.N).Bytes(), nil
}

func index(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		w.WriteHeader(404)
		return
	}
	const html = `<html>
	<style>
		.container { max-width: 600px; text-align: center; margin: 0 auto; font-size: 2em }
		p { font-family: monospace }
		p.scroll{ overflow-x: scroll }
	</style>
	<body>
		<main class="container">
			<img src="//vignette.wikia.nocookie.net/witcher/images/e/e2/Places_Rivia.png" />
			<p class="scroll">N: {{.N}}</p>
			<p>e: {{.E}}</p>
			<p class="scroll">CT: {{.CT}}</p>
		</main>
  </body>
</html>`
	t, err := template.New("html").Parse(html)
	panicIfError(err)

	prvKey, err := rsaGenerate()
	panicIfError(err)

	flagText := fmt.Sprintf("Well done! Here, have this for your troubles %s !", flag)
	ciphertext, err := rsaEncrypt([]byte(flagText), &prvKey.PublicKey)
	panicIfError(err)

	t.ExecuteTemplate(w, "html",
		struct {
			N  string
			E  int
			CT string
		}{
			N:  prvKey.PublicKey.N.String(),
			E:  3,
			CT: hex.EncodeToString(ciphertext),
		})
}

func main() {
	if port == "" || flag == "" {
		logger.Fatalf("invalid config")
	}

	mrand.Seed(time.Now().UnixNano())

	mux := http.NewServeMux()
	mux.HandleFunc("/", index)
	srv := &http.Server{
		Addr:         port,
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 10 * time.Second,
		IdleTimeout:  120 * time.Second,
		Handler:      mux,
	}

	logger.Println("server starting")
	err := srv.ListenAndServe()
	if err != nil {
		logger.Fatalf("server failed to start: %v", err)
	}
}

func panicIfError(err error) {
	if err != nil {
		logger.Fatal(err.Error())
	}
}
