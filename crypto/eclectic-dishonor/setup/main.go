package main

import (
	"bytes"
	"crypto/aes"
	"crypto/cipher"
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"encoding/base64"
	"fmt"
	"log"
	"net/http"
	"os"
	"text/template"
	"time"

	jose "github.com/square/go-jose"
)

var (
	port   = os.Getenv("CHALLENGE_PORT")
	flag   = os.Getenv("CHALLENGE_FLAG")
	logger = log.New(os.Stdout, "eclectic-dishonor ", log.LstdFlags|log.Lshortfile)
)

// ChatMessage .
type ChatMessage struct {
	From  string
	Value string
}

func buildChatScript() []ChatMessage {
	var err error

	var aliceKey *ecdsa.PrivateKey
	var aliceJWK string
	var aliceSecret []byte

	var bobKey *ecdsa.PrivateKey
	var bobJWK string
	var bobSecret []byte

	for {
		aliceKey, aliceJWK, err = dhGenerateJWK()
		bobKey, bobJWK, err = dhGenerateJWK()
		if err != nil {
			logger.Fatalf(err.Error())
		}

		aliceSecret = deriveSecretFromECDH(&bobKey.PublicKey, aliceKey)
		bobSecret = deriveSecretFromECDH(&aliceKey.PublicKey, bobKey)
		if !bytes.Equal(aliceSecret, bobSecret) {
			logger.Fatalf("wrong secret derivation")
		}

		// for some reason sometimes the derived secret is 31 bytes..
		if len(bobSecret) == 32 && len(aliceSecret) == 32 {
			break
		}
	}

	cipher, err := aes.NewCipher(aliceSecret)
	if err != nil {
		logger.Fatalf(err.Error())
	}

	chat := []ChatMessage{
		{From: "Butcher of Blaviken", Value: "i've got a task for you"},
		{From: "Butcher of Blaviken", Value: "3 beasts, piece of cake for you"},
		{From: "Geralt of Rivia", Value: "anything for the right coin"},
		{From: "Geralt of Rivia", Value: "a Djinn can snoop on my conversations.."},
		{From: "Geralt of Rivia", Value: "let's use E2E encryption"},
		{From: "Butcher of Blaviken", Value: fmt.Sprintf("ok, here's mine %s", bobJWK)},
		{From: "Geralt of Rivia", Value: fmt.Sprintf("got it. This is mine: %s", aliceJWK)},
		{From: "Geralt of Rivia", Value: "AES-ECB 256 never failed me"},
		{From: "Butcher of Blaviken", Value: "ok, let's do this"},
		{From: "Butcher of Blaviken", Value: ecbEncrypt([]byte("a fiesty Kikimora"), cipher)},
		{From: "Butcher of Blaviken", Value: ecbEncrypt([]byte(flag), cipher)},
		{From: "Butcher of Blaviken", Value: ecbEncrypt([]byte("and... a disgusting Striga!!!!!!!!"), cipher)},
		{From: "Geralt of Rivia", Value: ecbEncrypt([]byte("Hmm"), cipher)},
	}
	return chat
}

func dhGenerateJWK() (*ecdsa.PrivateKey, string, error) {
	prvKey, err := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	if err != nil {
		return nil, "", err
	}

	jwk := jose.JSONWebKey{Key: prvKey}
	jwkJSON, err := jwk.MarshalJSON()
	if err != nil {
		return nil, "", err
	}

	jwkJSONB64 := base64.RawURLEncoding.EncodeToString(jwkJSON)

	return prvKey, jwkJSONB64, nil
}

func ecbEncrypt(input []byte, cipher cipher.Block) string {
	paddedInput, _ := pkcs7Pad(input, cipher.BlockSize())
	blockSize := cipher.BlockSize()
	res := make([]byte, len(paddedInput))
	for i := 0; i < len(paddedInput); i += blockSize {
		cipher.Encrypt(res[i:i+blockSize], paddedInput[i:i+blockSize])
	}
	return base64.RawURLEncoding.EncodeToString(res)
}

func ecbDecrypt(input []byte, cipher cipher.Block) []byte {
	blockSize := cipher.BlockSize()
	if len(input)%blockSize != 0 {
		panic("input length is not divisible by block size")
	}
	res := make([]byte, len(input))
	for i := 0; i < len(input); i += blockSize {
		cipher.Decrypt(res[i:i+blockSize], input[i:i+blockSize])
	}
	return res
}

func deriveSecretFromECDH(theirPublic *ecdsa.PublicKey, myPrivate *ecdsa.PrivateKey) []byte {
	secret, _ := elliptic.P256().ScalarMult(theirPublic.X, theirPublic.Y, myPrivate.D.Bytes())
	return secret.Bytes()
}

func pkcs7Pad(input []byte, k int) ([]byte, error) {
	if !(k > 1) {
		return nil, fmt.Errorf("k must be greater than one - RFC5652")
	}
	if !(k < 256) {
		return nil, fmt.Errorf("this padding method is well defined if and only if k is less than 256 - RFC5652")
	}

	lth := len(input)
	paddingOctet := k - lth%k
	for i := 0; i < paddingOctet; i++ {
		input = append(input, byte(paddingOctet))
	}
	return input, nil
}

func index(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		w.WriteHeader(404)
		return
	}
	chat := buildChatScript()

	const html = `<html>
	<style>
		body { margin: 0; font-family: sans-serif }
		header { align-items: center; padding: 16px 32px; display: flex; flex-direction: row; justify-content: space-between; background: #ffd739 }
		header span { font-size: 2em }
		.container { margin: 32px 16px; display: flex; flex-direction: column }
		p { font-family: monospace }
		.bubble { 
			font-size: 16px; margin: 4px 0;     
			padding: 8px 20px;
			border-radius: 18px;
			color: white;
			margin: 4px 16px;
			max-width: 60%;
			text-align: left;
			overflow-wrap: break-word;
		}
		.alice {  
			background: #3f51b5; 
			text-align: right;     
			justify-content: flex-end;
			align-self: flex-end;
		}
		.bob { background: #1fca11; text-align: left; align-self: flex-start; justify-content: flex-start }
	</style>
	<body>
		<header>
		</header>
		<main class="container">
			{{ range .Chat }}
				<div class="bubble{{if (eq .From  "Geralt of Rivia")}} alice{{else}} bob{{end}}">
					{{ .Value }}
				</div>
			{{ end }}
		</main>
  </body>
</html>`
	t, err := template.New("html").Parse(html)
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte(err.Error()))
		return
	}
	t.ExecuteTemplate(w, "html",
		struct {
			Chat []ChatMessage
		}{
			Chat: chat,
		})
}

func main() {
	if port == "" || flag == "" {
		logger.Fatalf("invalid config")
	}

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
