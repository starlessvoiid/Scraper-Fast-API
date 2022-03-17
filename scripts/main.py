from fastapi import FastAPI
from scraper import Scraper
import json
import csv
from pprint import pprint
import pandas as pd

app = FastAPI() # Launching the app
scraper = Scraper() # Creating instance of Scraper object

@app.get("/{tag}")
async def read_data(tag) :

    return scraper.scrapemovies(tag) # Return scraped list of movie datas
@app.get("/{tag}/download")
async def read_data(tag) :

    data = scraper.scrapemovies(tag)

    with open(f"json_data_{tag}.txt", "w") as outfile :
        json.dump(data, outfile)
    
    df = pd.read_json (r'json_data_{tag}.txt')
    df.to_csv (r'data_csv_{tag}.csv', index = None)
    
    return "done"
