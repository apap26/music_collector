import os
import threading
from time import sleep

from pytube import Playlist
from pathlib import Path


def download_playlist(playlist_list, root_path):
    for playlist in playlist_list:
        p = Playlist(playlist)
        Path(root_path + p.title).mkdir(parents=True, exist_ok=True)
        for video in p.videos:
            name = video.title + video.author.title() + ".webm"
            name = (name.replace("/", "")
                    .replace("\\", "")
                    .replace(":", "")
                    .replace("*", "")
                    .replace("?", "")
                    .replace("\"", "")
                    .replace("<", "")
                    .replace(">", "")
                    .replace("|", ""))
            print("Downloading " + video.title)
            if (os.path.exists(root_path + p.title + "/" + name)) == False:
                try:
                    (video.streams.filter(type="audio")
                     .order_by('abr')
                     .desc()
                     .first()
                     .download(output_path=root_path + p.title, filename=name))
                    sleep(1)
                except:
                    print("failed to download " + video.title)
            else:
                print("Already downloaded")
