from pathlib import Path

import yandex
import youtube
import json


def __main__():
    with open("config.json", "r") as file:
        config = json.load(file)
        Path(config["yandex"]["root_path"]).mkdir(parents=True, exist_ok=True)
        yandex.yandex_download_favorite(config["yandex"]["token"], config["yandex"]["root_path"])
        Path(config["youtube"]["root_path"]).mkdir(parents=True, exist_ok=True)
        youtube.download_playlist(config["youtube"]["playlists"], config["youtube"]["root_path"])


if __name__ == "__main__":
    __main__()
