from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"
date = input("Which year do you want to travel to? Type date in YYYY-MM-DD format: ")

# get top 100 song chart for selected date
response = requests.get(f"{BILLBOARD_URL}/{date}")
website = response.text

# extract titles of the top 100 songs
soup = BeautifulSoup(website, "html.parser")
song_elements = soup.select(".o-chart-results-list__item .c-title")
song_titles = [song.getText().strip() for song in song_elements]

# connect to spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               cache_path="token.txt",
                                               scope="playlist-modify-private"))
user_id = sp.current_user()["id"]

# find tracks from the top 100 chart on spotify
playlist_tracks = []
for title in song_titles:
    searchRes = sp.search(q=f"track:{title}", type="track", limit=1)
    try:
        track = searchRes["tracks"]["items"][0]["uri"]
        playlist_tracks.append(track)
    except IndexError:
        pass

# create new playlist and save the tracks to it
playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)["id"]
sp.playlist_add_items(playlist_id, items=playlist_tracks)
