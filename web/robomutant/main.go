package main

import (
	"log"
	"net/http"
	"os"
	"time"
)

var (
	port   = os.Getenv("CHALLENGE_PORT")
	flag   = os.Getenv("CHALLENGE_FLAG")
	logger = log.New(os.Stdout, "robosushi ", log.LstdFlags|log.Lshortfile)
)

func secret(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/super-duper-secret" {
		w.WriteHeader(http.StatusNotFound)
		w.Write([]byte("Are you lost?"))
		return
	}
	w.WriteHeader(http.StatusUnauthorized)
	w.Write([]byte(flag))
	return
}

func robots(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/robots.txt" {
		w.WriteHeader(404)
		return
	}
	text := `User-agent: *
Disallow: /super-duper-secret`
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(text))
}

func index(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		w.WriteHeader(404)
		return
	}
	const html = `<html>
	<link href="//fonts.googleapis.com/css?family=Nosifer&display=swap" rel="stylesheet">
	<style>
		body { margin: 0; font-family: 'Nosifer', cursive; }
		.container { max-width: 600px; text-align: center; margin: 64px auto; font-size: 2em }
	</style>
	<body>
		<main class="container">
			<h1>RoboMutant</h1>
			<p>What the hell is a robomutant??</p>
		</main>
  </body>
</html>`
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(html))
}

func main() {
	if port == "" || flag == "" {
		logger.Fatalf("invalid config")
	}

	mux := http.NewServeMux()

	mux.HandleFunc("/super-duper-secret", secret)
	mux.HandleFunc("/robots.txt", robots)
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
