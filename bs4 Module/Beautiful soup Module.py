from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)
