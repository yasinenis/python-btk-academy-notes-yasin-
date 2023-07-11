# UYGULAMA

import requests

# themoviedb.org => film ve dizi arjivi
# themoviedb' nin sunduğu apiyi uygulamanızda kullanınız.
# anahtar kelimeye göre arama
# En populer film listesi
# Vizyondaki film listesi

class theMovieDB:
    def __init__(self):
        self.api_url = "https://moviesminidatabase.p.rapidapi.com" # link kestik
        self.headers = {
            "X-RapidAPI-Key": "-need a API key here-",
	        "X-RapidAPI-Host": "need an API host here"
        }

    def getPopulars(self):
        response = requests.get(self.api_url+"/movie/order/byPopularity/", headers = self.headers)
        return response.json()

    def getSearchResults(self, keyword):
        response = requests.get(self.api_url+"/movie/imdb_id/byTitle/"+keyword+"/",headers=self.headers)
        return response.json()


movieApi = theMovieDB()







while True:
    secim = input("\n1- Popular Movies\n2- Search Movies\n3- Exit\n\nSeçiminiz: ")
    
    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])

        if secim == "2":
            keyword = input("keyword: ")
            movies = movieApi.getSearchResults(keyword)
            for movie in movies['results']:
                print(movie['title'])
    











#------------

url = "https://moviesminidatabase.p.rapidapi.com/movie/order/byPopularity/"

headers = {
	"X-RapidAPI-Key": "914940287dmshc56772138087190p177405jsn52c96499d493",
	"X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())

#------------