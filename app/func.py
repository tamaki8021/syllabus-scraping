import requests
from bs4 import BeautifulSoup

def setup(url):
    url = requests.get(url)

    soup = BeautifulSoup(url.content, "html.parser")
    return url, soup
