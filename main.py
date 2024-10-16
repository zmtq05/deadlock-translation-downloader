import gdown
import os
import time

dir = os.path.join(
    os.getenv("LOCALAPPDATA", os.getcwd()), "Deadlock translation downloader"
)
os.makedirs(dir, exist_ok=True)
game_path_fname = os.path.join(dir, "path.txt")
translation_url = "https://drive.google.com/uc?id=1eYAZiLb6xmNQZw-sxh1mJWshTC6xHLJz"
font_url = "https://drive.google.com/uc?id=1t2lh6KPnTkBoM_-PPFmx5CRBum-gLb31"

if not os.path.exists(game_path_fname):
    while True:
        game_path = input("Deadlock 폴더 위치: ")
        if not os.path.exists(game_path):
            print("Error: 폴더가 존재하지 않음")
        else:
            break

    with open(game_path_fname, "w") as file:
        file.write(game_path)
        print(f"게임 경로가 {game_path_fname}에 저장됨")

else:
    with open(game_path_fname, "rt") as file:
        game_path = file.read().rstrip()


def download(url, output, msg):
    print(msg)
    try:
        gdown.download(url, output)
        gdown.extractall(output, game_path)
        if os.path.exists(output):
            os.remove(output)
        print("완료")
    except Exception as e:
        print(f"Error downloading {output}: {e}")


timestamp = int(time.time())
download(font_url, f"font_{timestamp}.zip", "맞춤 폰트 다운로드")
download(translation_url, f"translation_{timestamp}.zip", "번역 다운로드")
