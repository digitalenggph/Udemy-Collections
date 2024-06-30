import os
import requests
import spotipy

from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# -------------------------------------------------SPOTIFY API DETAILS------------------------------------------------ #
SPOTIFY_USERNAME = os.environ.get("ENV_SPOTIFY_USERNAME")
# -----------------------------------------------------CODE BLOCK---------------------------------------------------- #
# input date
time_travel_to = input("Which date would you like to be taken back? YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{time_travel_to}/"

# TODO 1: Use bs4 to scrape songs from the date of you choice
response = requests.get(URL)
song_hits = response.text

soup = BeautifulSoup(song_hits, "html.parser")
song_book = soup.select("div.o-chart-results-list-row-container ul li")

class_ = ['c-label', 'a-no-trucate', 'a-font-primary-s', 'lrv-u-font-size-14@mobile-max', 'u-line-height-normal'
                                                                                          '@mobile-max',
          'u-letter-spacing-0021', 'lrv-u-display-block', 'a-truncate-ellipsis-2line', 'u-max-width-330',
          'u-max-width-230@tablet-only']
class_1 = ['c-label', 'a-no-trucate', 'a-font-primary-s', 'lrv-u-font-size-14@mobile-max', 'u-line-height-normal'
                                                                                           '@mobile-max',
           'u-letter-spacing-0021', 'lrv-u-display-block', 'a-truncate-ellipsis-2line', 'u-max-width-330',
           'u-max-width-230@tablet-only', 'u-font-size-20@tablet']

# TODO 2: Get list of songs from URL
song_list = [song.h3.getText().strip() for song in song_book
             if song.h3 is not None]

song_list_cleaned = [song for index, song in enumerate(song_list)
                     if index % 2 == 0]

singer_list = [song.span.getText().strip() for song in song_book
               if song.span is not None
               if song.span['class'] in [class_, class_1]]

singer_list_cleaned = [singer for index, singer in enumerate(singer_list)
                       if index % 2 == 0]

# TODO 3: Use Spotify API to create playlist

scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

playlist_name = f"Take me back to {time_travel_to} :)"
playlist_description = f"This playlist is the Top 100 hits for {time_travel_to}"

playlist = sp.user_playlist_create(user=SPOTIFY_USERNAME, name=playlist_name, public=True, collaborative=False,
                                   description=playlist_description)
playlist_id = playlist['id']

client_credentials_manager = SpotifyClientCredentials()
sp_search = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

song_dict = {}
songs_to_add = []
check = None

for i in range(len(song_list_cleaned)):
    song = song_list_cleaned[i]
    singer = singer_list_cleaned[i]
    q = f"name:{song}%artist:{singer}"
    search = sp_search.search(q=q, type="track")
    song_dict[song] = {
        "artist": singer,
        "search": search
    }

    for item in song_dict[song]['search']['tracks']['items']:
        for artist in item['artists']:
            artist_string_list = artist['name'].lower().split()
            singer_string_list = singer.lower().split()

            range_len = min(len(artist_string_list), len(singer_string_list))

            for index in range(range_len):
                if len(artist_string_list) < len(singer_string_list):
                    check = artist_string_list[index] in singer_string_list
                else:
                    check = singer_string_list[index] in artist_string_list

            if check:
                uri = item['uri']
                if uri not in songs_to_add:
                    print(i, song, singer, uri)
                    songs_to_add.append(uri)
        break

sp.playlist_add_items(playlist_id, songs_to_add)
