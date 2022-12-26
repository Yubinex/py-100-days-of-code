from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

# billboard code
date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url="https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_names = [song.getText().strip() for song in song_names_spans]

with open("Proj42-SpotifyPlaylist/token.txt") as token_file:
    spotify_token = token_file.read()
with open("Proj42-SpotifyPlaylist/secret.txt") as secret_file:
    spotify_secret = secret_file.read()

# spotipy code
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_token,
        client_secret=spotify_secret,
        show_dialog=True,
        cache_path="Proj42-SpotifyPlaylist/cache_token.txt",
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split('-')[0]
for song in song_names:
    res = sp.search(q=f"track:{song} year:{year}", type="track")
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(res)
    try:
        uri = res["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on Spotify. SKIPPED.")

# create playlist
playlist_name = f"{date} Billboard 100"
playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    collaborative=False,
    description=f"Top 100 songs of {date.split('-')[0]}."
)
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)
