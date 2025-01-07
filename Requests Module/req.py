import requests

url = "https://github.com/AkhileshAher"
r =requests.get(url)
print(r.text)
