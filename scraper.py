import json
import re

import requests
from bs4 import BeautifulSoup

URL = "https://www.nytimes.com/puzzles/spelling-bee"


def extract_chars(soup):
    def extract_javascript(soup):
        return str(soup.find(id="js-hook-pz-moment__game").script.string)

    def extract_game_data(js):
        extracted = re.search("window\.gameData = (.*)", js)
        return json.loads(extracted.group(1))

    js = extract_javascript(soup)
    game_data = extract_game_data(js)

    return game_data["today"]["centerLetter"], game_data["today"]["outerLetters"]


def fetch_chars():
    content = requests.get(URL).text
    soup = BeautifulSoup(content, "html.parser")

    return extract_chars(soup)
