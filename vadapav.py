import requests
from bs4 import BeautifulSoup as bs

url = "https://vadapav.mov/2c4a1ef9-2604-4d53-8441-f6930d22d131/"

response = requests.get(url)
soup = bs(response.text, "html.parser")

file_links = []

for i in soup.find_all("li"):
    try:
        url = "https://vadapav.mov" + i.find("a")["href"]
        file_links.append(url)
    except:
        pass

with open("links.txt", "w") as f:
    for i in file_links[1:]:
        f.write(i + "\n")
