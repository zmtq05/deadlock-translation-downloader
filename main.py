import gdown
import os
import toml
import requests
from bs4 import BeautifulSoup

config_file_path = "config.toml"

if not os.path.exists(config_file_path):
    while True:
        game_path = input("Deadlock 폴더 위치: ")
        if not os.path.exists(game_path):
            print("Error: 폴더가 존재하지 않음")
        else:
            break

    config = {
        "settings": {
            "translation_post_url": "https://gall.dcinside.com/mgallery/board/view/?id=deadlock&no=1034",
            "game_path": game_path,
        }
    }

    with open(config_file_path, "w") as file:
        toml.dump(config, file)

else:
    with open(config_file_path, "r") as file:
        config = toml.load(file)
        game_path = config["settings"]["game_path"]

translation_post_url = config["settings"]["translation_post_url"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
response = requests.get(translation_post_url, headers=headers)
if response.status_code != 200:
    input("게시글이 존재하지 않습니다. Enter를 눌러 종료")
    exit()
soup = BeautifulSoup(response.text, "html.parser")

p_list = soup.select("#temp_og_paste_box p:has(a > span)")
for p in p_list:
    for sibling in p.next_siblings:
        text = sibling.get_text()
        if "번역" in text:
            translation_url = p.get_text()
            break
        elif "맞춤" in text:
            font_url = p.get_text()
            break


output = "translation.zip"
print("번역 다운로드")
gdown.download(translation_url, output=output, fuzzy=True)
gdown.extractall(output, game_path)
os.remove(output)

output2 = "font.zip"
print("맞춤 폰트 다운로드")
gdown.download(font_url, output=output2, fuzzy=True)
gdown.extractall(output2, game_path)
os.remove(output2)

input("Enter를 눌러 종료")
