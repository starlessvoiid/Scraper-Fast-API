import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

#Scraper class
class Scraper() :

    

    def scrapemovies(self, tag) :

        # Return variables
        movies_data = []

        pages = [1]

        # Looping through all pages
        for page in pages :
            url = f"https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres={tag}&start={str(page)}&ref_=adv_nxt"
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            movie_data = soup.findAll("div", attrs = {"class" : "lister-item mode-advanced"}) # Find movie section
            sleep(randint(2, 8)) # To avoid crashing

            for item in movie_data : # Loop through each item

                item = {
                    "name" : item.h3.a.text, #Scrape the name of the movie

                    "year" : item.h3.find("span", class_ = "lister-item-year text-muted unbold").text.replace("(", "").replace(")", ""), # Scrape the year of release

                    "rating" : item.find("div", class_ = "inline-block ratings-imdb-rating").text.strip(), # Scrape the rating of movies

                    "genre" : item.p.find("span", class_ = "genre").text.strip(), # Scrape the genre

                    "description" : item.findAll("p", class_ = "text-muted")[1].text.replace("\n", "") # Scrape the description of the movie
                }

                movies_data.append(item)
                
        return movies_data # return a JSON of movie items