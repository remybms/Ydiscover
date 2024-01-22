package main

import (
	"meteo"
	"net/http"
)

func main() {
	db := meteo.OpenDb()
	meteo.InitDb(db)
	defer db.Close()
	http.Handle("/static/", http.StripPrefix("/static", http.FileServer(http.Dir("template"))))
	//risque := meteo.Resultat()
	http.HandleFunc("/", meteo.Accueil)
	http.HandleFunc("/inscription", func(w http.ResponseWriter, r *http.Request) {
		meteo.Inscription(w, r)
	})
	http.HandleFunc("/connexion", func(w http.ResponseWriter, r *http.Request) {
		meteo.Connexion(w, r)
	})
	http.HandleFunc("/compte", func(w http.ResponseWriter, r *http.Request) {
		meteo.Compte(w, r)
	})
	http.ListenAndServe(":8080", nil)

}
