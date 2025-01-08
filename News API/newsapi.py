import requests
import json

query = input("What type of news are you intrested in ?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-01-07&to=2025-01-07&sortBy=popularity&apiKey=--------------------Your API Key-------------------"

r = requests.get(url)

news = json.loads(r.text)

# print(news,type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------------------------")
