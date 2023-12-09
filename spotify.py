import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config


SPOTIPY_CLIENT_ID = config('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = config('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = config('SPOTIPY_REDIRECT_URI')

playlist_name = 'List'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope='playlist-read-private'
))

playlists = sp.current_user_playlists()

playlist_id = None
for playlist in playlists['items']:
    if playlist['name'] == playlist_name:
        playlist_id = playlist['id']
        break

if playlist_id:
    results = sp.playlist_tracks(playlist_id)
    for track in results['items']:
        track_name = track['track']['name']
        artist_names = ', '.join(
            [artist['name'] for artist in track['track']['artists']]
        )
        print(f"{artist_names} - {track_name}")
else:
    print(f"Плейлист с именем '{playlist_name}' не найден.")
