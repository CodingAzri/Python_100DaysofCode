import requests
from bs4 import BeautifulSoup
from pprint import PrettyPrinter
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

pp = PrettyPrinter()
# Website scraping from Billboard 100
date = input("Which year do you want to travel to? Type in this format YYYY-MM-DD: ")
year = date[:4]

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
CLIENT_ID_SPOTIFY = os.environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET_ID = os.environ.get("SPOTIFY_CLIENT_SECRET")
USERNAME = os.environ.get("USERNAME")

response = requests.get(URL)
billboard_website = response.text

soup = BeautifulSoup(billboard_website, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
# pp.pprint(song_names)

# Spotify API
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID_SPOTIFY,
        client_secret=CLIENT_SECRET_ID,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,
    ))

user_id = sp.current_user()["id"]

# Search songs in Spotify
song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# print(song_uris)

# Create a playlist for the list or song uris
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
