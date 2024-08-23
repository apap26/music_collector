import os
import re
from yandex_music import Client



def yandex_download_favorite(tk, directory):
    client = Client(tk).init()
    tracks = client.users_likes_tracks().fetchTracks()
    for i in tracks:
        title = (i.title
                 .replace("/", "")
                 .replace("\\", "")
                 .replace(":", "")
                 .replace("*", "")
                 .replace("?", "")
                 .replace("\"", "")
                 .replace("<", "")
                 .replace(">", "")
                 .replace("|", ""))
        name = directory + title + " - " + i.artistsName()[0] + ".mp3"
        if (os.path.exists(name)) == False:
            i.download(name)
            print("Downloaded " + name)
        else:
            print("skip " + name)