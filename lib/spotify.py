import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials

scope = "user-read-recently-played"

spotifyObjct = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=credentials.client_ID, client_secret= credentials.client_SECRET, redirect_uri=credentials.redirect_url, scope=scope))

results = spotifyObjct.current_user_recently_played()
for idx, item in enumerate(results['items']):
  track = item['track']
  print(idx, track['artists'][0]['name'], " – ", track['name'])
