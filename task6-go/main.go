package main

import (
    "fmt"
    "net/http"
    "time"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "<h1>Hello, World!</h1>")
    fmt.Fprintf(w, "<p>From Go Application</p>")
    fmt.Fprintf(w, "<p>Current time: %s</p>", time.Now().Format(time.RFC1123))
}

func main() {
    http.HandleFunc("/", handler)
    port := ":8080"
    fmt.Printf("Starting Go server on port %s\n", port)
    http.ListenAndServe(port, nil)
}
