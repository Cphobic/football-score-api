import requests

url = "https://davidesantangelo-scrappet-v1.p.rapidapi.com/api/scrape"

querystring = {"url": "http://rapidapi.com"}

headers = {
    'x-rapidapi-host': "davidesantangelo-scrappet-v1.p.rapidapi.com",
    'x-rapidapi-key': "d7883b3dfcmsh96929a15fb5fdbep1ac876jsn8a640532b6f7"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
