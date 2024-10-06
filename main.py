import gdown
import os
import toml
import requests
from bs4 import BeautifulSoup

config_file_path = "config.toml"

if not os.path.exists(config_file_path):
    game_path = input("Deadlock game path: ")

    config = {
        "settings": {
            "translation_url": "https://gall.dcinside.com/mgallery/board/view/?id=deadlock&no=1034",
            "game_path": game_path
        }
    }

    with open(config_file_path, "w") as file:
        toml.dump(config, file)


else:
    with open(config_file_path, "r") as file:
        config = toml.load(file)
        game_path = config["settings"]["game_path"]

translation_url = config["settings"]["translation_url"]

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(translation_url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

url = soup.select_one('#temp_og_paste_box a')['href'] # pyright: ignore

output="temp.zip"
gdown.download(url, output=output, fuzzy=True)
gdown.extractall(output, game_path)
# os.remove(output)
