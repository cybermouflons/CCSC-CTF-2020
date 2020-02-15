package main

import (
	"log"
	"net/http"
	"os"
	"strings"
	"time"

	"github.com/dgrijalva/jwt-go"
)

var (
	port   = os.Getenv("CHALLENGE_PORT")
	flag   = os.Getenv("CHALLENGE_FLAG")
	secret = os.Getenv("CHALLENGE_SECRET")
	logger = log.New(os.Stdout, "just-wraith-trouble ", log.LstdFlags|log.Lshortfile)
)

func admin(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/admin" {
		w.WriteHeader(http.StatusNotFound)
		w.Write([]byte("Are you lost?"))
		return
	}

	cookie, err := r.Cookie("session")
	if err != nil || cookie == nil {
		w.WriteHeader(http.StatusUnauthorized)
		w.Write([]byte("Unauthorized. Please go away."))
		return
	}

	usingAlgNone := false
	token, err := jwt.Parse(cookie.Value, func(token *jwt.Token) (interface{}, error) {
		return []byte(secret), nil
	})
	if err != nil {
		// good thing these libraries make it hard to use "alg": "none" xD
		if err.Error() == "'none' signature type is not allowed" {
			usingAlgNone = true
		} else {
			logger.Println(err.(*jwt.ValidationError).Errors)
			w.WriteHeader(http.StatusUnauthorized)
			w.Write([]byte(err.Error()))
			return
		}
	}

	isAdmin := func(claims map[string]interface{}) bool {
		role, roleExists := claims["role"]
		if roleExists && strings.EqualFold(role.(string), "admin") {
			return true
		}
		return false
	}

	claims, ok := token.Claims.(jwt.MapClaims)
	if ok && token.Valid {
		if isAdmin(claims) {
			w.WriteHeader(http.StatusOK)
			w.Write([]byte(flag))
			return
		}
	} else if ok && usingAlgNone {
		if isAdmin(claims) {
			w.WriteHeader(http.StatusOK)
			w.Write([]byte(flag))
			return
		}
	}

	w.WriteHeader(http.StatusUnauthorized)
	w.Write([]byte("Go away."))
	return
}

func index(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		w.WriteHeader(404)
		return
	}
	const html = `<html>
	<style>
		body { margin: 0 }
		header { align-items: center; padding: 16px 32px; font-size: 18px; display: flex; flex-direction: row; justify-content: space-between; background: #ffd739 }
		header span { font-size: 2em }
		header a { font-size: 1.25em; color: #000; text-decoration: none }
		.container { max-width: 600px; text-align: center; margin: 0 auto; font-size: 2em }
		p { font-family: monospace }
	</style>
	<body>
		<header>
			<a href="/"><span alt="ghost emoji">👻</span></a>
			<a href="/admin">Admin</a>
		</header>
		<main class="container">
			<img src="//vignette.wikia.nocookie.net/witcher/images/c/c6/Tw3_journal_wraith.png">
			<p>muahahahhaha</p>
		</main>
  </body>
</html>`

	// Create a new token object, specifying signing method and the claims
	// you would like it to contain.
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"role": "demo_account",
		"iss":  time.Now().Unix(),
	})

	// Sign and get the complete encoded token as a string using the secret
	tokenString, err := token.SignedString([]byte(secret))
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte(err.Error()))
		return
	}

	cookie := http.Cookie{Name: "session", Value: tokenString}
	http.SetCookie(w, &cookie)
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(html))
}

func main() {
	if port == "" || flag == "" {
		logger.Fatalf("invalid config")
	}

	mux := http.NewServeMux()

	mux.HandleFunc("/admin", admin)
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
