import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import re

print("Starting Spotify...")
scope = ["user-read-currently-playing","user-modify-playback-state"]
api = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


results = api.currently_playing()


def get_current_song() -> str:
    results = api.currently_playing()
    if results is None: return f"Nothing is currently playing."
    artist = results['item']['artists'][0]['name']
    song_title = results['item']['name']
    return f"Now Playing: {artist} - {song_title}" 

def next_song(): 
    results = api.currently_playing()
    if results is None: return f"Spotify isn't active"
    api.next_track()

def prev_song(): 
    results = api.currently_playing()
    if results is None: return f"Spotify isn't active"
    api.previous_track()

def queue_song(uri: str) -> str:
    if uri is None: return f'Please enter a valid Spotify URL (uri is none)'
    try:
        api.add_to_queue(uri)
    except Exception as e:
        return f'Error adding song to queue: {e}'
    
    return 'Adding song to queue...'
