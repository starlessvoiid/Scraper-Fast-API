from requests_html import HTMLSession

class Scraper() :

    def scrapedata(self, tag) :
        url = f"https://www.imdb.com/search/title/?genres={tag}&explore=title_type,genres&ref_=tt_ov_inf"
        s = HTMLSession()
        r = s.get(url)
        print(r.status_code)

movies = Scraper()
movies.scrapedata("Action")