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
 * Control the orbitals to gain the power of Angel Fire
 */

var (
	port   = os.Getenv("CHALLENGE_PORT")
	flag   = os.Getenv("CHALLENGE_FLAG")
	logger = log.New(os.Stdout, "harlans-world", log.LstdFlags|log.Lshortfile)
)

func rsaGenerate() (*rsa.PrivateKey, error) {
	prvKey := &rsa.PrivateKey{}
	var big1 = big.NewInt(1)
	var big3 = big.NewInt(3)

	for {
		var err error
		var p *big.Int
		var q *big.Int

		p, err = rand.Prime(rand.Reader, 512)
		q, err = rand.Prime(rand.Reader, 512)
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
			<img src="//https://vignette.wikia.nocookie.net/altered-carbon/images/d/d5/Harlansworldtwo.jpg" />
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

	flagText := fmt.Sprintf("Congratulations %s !", flag)
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
