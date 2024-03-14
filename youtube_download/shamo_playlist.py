from pytube import Playlist
from user_input import *
from shamo_videos import shamo_videos


def shamo_playlist():

    while True:
        try:
            playlists = [Playlist(link) for link in get_links()]
            break

        except Exception as e:
            print(e)

    # print(playlists)
    [print(f"{i+1} | Playlist title: {playlist.title:<40} | No. vidoes: {playlist.length}")
     for i, playlist in enumerate(playlists)]

    selection: list[Playlist] = get_selection(playlists)

    if get_confirm("Continue"):
        [shamo_videos(playlist.videos, playlist.title)
         for playlist in selection]


if __name__ == "__main__":
    shamo_playlist()
