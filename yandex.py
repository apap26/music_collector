import os
import re
from pathlib import Path

import unicodedata
from yandex_music import Client

def remove_forbidden_symbols(string):
    value = str(string)
    value = unicodedata.normalize('NFKC', value)
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def yandex_download_favorite(tk, directory):
    client = Client(tk).init()
    tracks = client.users_likes_tracks().fetchTracks()
    for i in tracks:
        title = remove_forbidden_symbols(i.title)
        name = directory + title + " - " + i.artistsName()[0] + ".mp3"
        if (os.path.exists(name)) == False:
            i.download(name)
            print("Downloaded " + name)
        else:
            print("skip " + name)


def yandex_download_playlists(tk, playlists_ids, dir_name):
    for playlist_id in playlists_ids:
        yandex_download_playlist(tk, playlist_id, dir_name)

def yandex_download_playlist(tk, playlist_id, dir_name):
    client = Client(tk).init()
    album = client.albums_with_tracks(playlist_id)
    album_title = remove_forbidden_symbols(album.title)
    Path(dir_name + album_title).mkdir(parents=True, exist_ok=True)
    for tracks in album.volumes:
        for track in tracks:
            title = remove_forbidden_symbols(track.title)
            name = dir_name + album_title + "\\" + title + " - " + track.artistsName()[0] + ".mp3"
            if (os.path.exists(name)) == False:
                track.download(name)
                print("Downloaded " + name)
            else:
                print("skip " + name)