import bs4
import requests
import cutlet
import json

#Romaji translation without using foreign spelling
katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False

BASE_URL = "https://www.freem.ne.jp"
BASE_PAGE_URL = BASE_URL + "/win/category/4/page-"
page = 0

def get_source(url):
    r = requests.get(url)
    return bs4.BeautifulSoup(r.text, "html.parser")

def get_games(src):
    listgame = src.find("ul", {"class":"game-list-wrap"})
    urls = None
    if listgame is not None:
        urls = []
        for game in listgame.findChildren("li", recursive=False):
            if "sp-ad-list" not in game.get("class"):
                urls.append(BASE_URL + game.find("a")["href"])

    return urls

def get_game_info(src):
    game = {}
    
    game["title"]= {}
    game["title"]["original"] = src.find("h1").getText().strip()
    game["title"]["romaji"] = katsu.romaji(game["title"]["original"])

    details = src.find("table", {"class":"game-detail-table"})

    for detail in details.findChildren("tr", recursive=False):
        entry = detail.th.text.strip()

        if entry == "[OS]":
            os = detail.td.text.strip().lower()
            game["os"] = []
            
            if "win" in os or "browser" in os:
                if "win" in os:
                    game["os"].append("Windows")
                if "browser" in os:
                    game["os"].append("Browser")
            else:
                game["os"].append(os)

        if entry == "[Registered]":
            game["date"] = detail.td.text.strip()
        
        if entry == "[Content Rating]":
            game["rating"] = detail.td.text.strip()

    namediv = src.find("div", {"class":"game-creator-name"})

    game["author"] = {}
    game["author"]["original"] = namediv.h3.a.string.strip()
    game["author"]["romaji"] = katsu.romaji(game["author"]["original"])


    return game

def main():

    games = []
    while True:
        src = get_source(BASE_PAGE_URL + str(page))
        games_urls = get_games(src)

        if games_urls is not None:
            for url in games_urls:
                src = get_source(url)
                game_infos = get_game_info(src)
                game_infos["url"] = url
                games.append(game_infos)
        else:
            break

        page += 1

    with open("games.json", "w+", encoding="utf-8") as f:
        json.dump(games, f, indent=4, ensure_ascii=False)


if "__main__" == __name__:
    main()

