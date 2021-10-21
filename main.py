from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.freem.ne.jp/"
BASE_PAGE_URL = BASE_URL + "win/category/4/page-"
page = 0

def get_source(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, "html.parser")

def main():
    #src = get_source(BASE_PAGE_URL + str(page))
    src = ""
    with open("index.html", "r", encoding="utf-8") as f:
        src = BeautifulSoup(f.read(), "html.parser")
    
    listgame = src.find("ul", {"class":"game-list-wrap"})

    for game in listgame.findChildren("li", recursive=False):
        if "sp-ad-list" not in game.get("class"):
            print(game.find("a")["href"])

if "__main__" == __name__:
    main()

