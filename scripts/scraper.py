import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

#Scraper class
class Scraper() :

    movie_name = []
    year = []
    rating = []
    genre = []
    
    pages = [page for page in range(1, 1000, 50)]

    def scrapemovies(self, tag) :
        for page in pages :
            url = f"https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres={tag}&start={page}&ref_=adv_nxt"
        s = HTMLSession()
        r = s.get(url)
        print(r.status_code)

        movies_list = []

        movies = r.html.find("div.lister-item-content")

        for m in movies :
            print(m.find("p.text-muted", first = False))

movies = Scraper()
movies.scrapedata("Action")