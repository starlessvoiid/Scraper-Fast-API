from fastapi import FastAPI
from scraper import Scraper
import json
import csv
from pprint import pprint

app = FastAPI() # Launching the app
scraper = Scraper() # Creating instance of Scraper object

@app.get("/{tag}")
async def read_data(tag) :

    return scraper.scrapemovies(tag) # Return scraped list of movie datas
@app.get("/{tag}/download")
async def read_data(tag) :

    data = scraper.scrapemovies(tag)
    json_data = json.dumps(data)

    return json_data

    with open(f"data_{tag}",'wb') as file:
        output_csv = csv.writer(file)
        output_csv.writerows(json_data)
