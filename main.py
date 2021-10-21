from bs4 import BeautifulSoup
import requests
import cutlet

#Romaji translation without using foreign spelling
katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False

BASE_URL = "https://www.freem.ne.jp"
BASE_PAGE_URL = BASE_URL + "/win/category/4/page-"
page = 0

def get_source(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, "html.parser")

def get_games(src):
    listgame = src.find("ul", {"class":"game-list-wrap"})
    urls = []
    for game in listgame.findChildren("li", recursive=False):
        if "sp-ad-list" not in game.get("class"):
            urls.append(BASE_URL + game.find("a")["href"])

    return urls

def get_game_info(src):
    game = {}
    
    game["title"] = src.find("h1").getText().strip()
    game["title_romaji"] = katsu.romaji(game["title"])

    return game

def main():
    #src = get_source(BASE_PAGE_URL + str(page))
    src = ""
    with open("game.html", "r", encoding="utf-8") as f:
        src = BeautifulSoup(f.read(), "html.parser")

        print(get_game_info(src))



if "__main__" == __name__:
    main()

