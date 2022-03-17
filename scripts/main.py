from fastapi import FastAPI
from scraper import Scraper

app = FastAPI() # Launching the app
scraper = Scraper() # Creating instance of Scraper object

@app.get("/{tag}")
async def read_data(tag) :

    return scraper.scrapemovies(tag) # Return scraped list of movie datas