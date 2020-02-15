package main

import (
	"crypto/aes"
	"crypto/ecdsa"
	"encoding/base64"
	"fmt"
	"strings"
	"testing"

	jose "github.com/square/go-jose"
)

func TestSolution(t *testing.T) {
	aliceJWKBase64 := "eyJrdHkiOiJFQyIsImNydiI6IlAtMjU2IiwieCI6IlJnT2JJWnJuM3FCdVhvSGJkSUpub3lCOWZsRWo2azJaX283RGl0NHZDTUkiLCJ5IjoiTHJfUWthNUM2aDk4M3VwWWtXMURGRFlIWDJoOVYzNVlNaC1tUXNUaXNyMCIsImQiOiJNa3dtMzUyWmZIdnlpc29mMlowbnowaklTV3JKUGZFc042bkxrMUJ6QkNBIn0"
	aliceJWKBytes, _ := base64.RawURLEncoding.DecodeString(aliceJWKBase64)
	aliceJWK := jose.JSONWebKey{}
	aliceJWK.UnmarshalJSON(aliceJWKBytes)
	aliceKey := aliceJWK.Key

	bobJWKBase64 := "eyJrdHkiOiJFQyIsImNydiI6IlAtMjU2IiwieCI6IjRNZ2ZVczN4b21VUkdCMEVpZ3R1ejNSTE1kZ1JXdnJsZWhvVmpQSmFBeTgiLCJ5Ijoib2RVTVpVQzc0dUs5VzhuZzFqS2xSMDZJMkJ4bVFKdWlINzhWa2NBeTFnayIsImQiOiI3aVR5VDZuQ0tvbGhVaVFlbk9vVTF6bkdZQXVDdVFUTmxJdk1ZUGt4WjFBIn0"
	bobJWKBytes, _ := base64.RawURLEncoding.DecodeString(bobJWKBase64)
	bobJWK := jose.JSONWebKey{}
	bobJWK.UnmarshalJSON(bobJWKBytes)
	bobKey := bobJWK.Key

	secret := deriveSecretFromECDH(&aliceKey.(*ecdsa.PrivateKey).PublicKey, bobKey.(*ecdsa.PrivateKey))

	cipher, _ := aes.NewCipher(secret)
	ct1, _ := base64.RawURLEncoding.DecodeString("T6sNybtrsc2Kwz9QkiKBOF29FqH1zgAL1dypbSl0VSg")
	ct2, _ := base64.RawURLEncoding.DecodeString("JqwMR5FW1upxzOscza8LTLHqzpdjZZtnPcr3h6BEsS8")
	ct3, _ := base64.RawURLEncoding.DecodeString("bNEWQLtnJUQDPjwAW38Tlxyt_z40ds9O-Ks5vxVVVTQ")
	ct4, _ := base64.RawURLEncoding.DecodeString("I_FbAX2YoUJX0YOvj6Lx0m-ZbquEFCtsUYfw7vCaPsc")

	pt1 := ecbDecrypt(ct1, cipher)
	pt2 := ecbDecrypt(ct2, cipher)
	if !strings.Contains(string(pt2), flag) {
		t.Fatalf("invalid flag decryption")
	}
	pt3 := ecbDecrypt(ct3, cipher)
	pt4 := ecbDecrypt(ct4, cipher)

	fmt.Println(string(pt1))
	fmt.Println(string(pt2))
	fmt.Println(string(pt3))
	fmt.Println(string(pt4))
}
