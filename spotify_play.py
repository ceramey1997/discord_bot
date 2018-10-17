import spotipy
import json
import spotipy.util as util

import discord
from discord.ext import commands
import asyncio

username = 'xxmyp4fglpr2bry8o91266vx8'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
SPOTIPY_CLIENT_ID = '66991a05186c41e79b6621d794ffaabb'
SPOTIPY_CLIENT_SECRET = '847a0ff59a39484882ddfa6087e24a5a'
SPOTIPY_REDIRECT_URI = 'http://www.google.com/'

token = util.prompt_for_user_token(username,
                                   scope,
                                   client_id=SPOTIPY_CLIENT_ID,
                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                   redirect_uri=SPOTIPY_REDIRECT_URI)
spotifyObject_main = spotipy.Spotify(auth=token)

class SpotifyHandle(object):

    def _song_json_resp(song_name, spotifyObject):
        # song_name = input("Input Song Name Here: \n>>> ")
        resp = spotifyObject.search(song_name, limit=1, type='track', market='US')
        return resp

    # redo variables inside this function
    def _get_track_uri(song_name):
        track_info = _song_json_resp(song_name, spotifyObject_main)
        return track_info['tracks']['items'][0]['uri']

    def get_device(spotifyObject):
        devices = spotifyObject.devices()
        deviceID = devices['devices'][0]['id']
        return deviceID

    def get_current_track_info(spotifyObject):
        track = spotifyObject.current_user_playing_track()
        artist = track['item']['artists'][0]['name']
        track = track['item']['name']

        if artist != "":
            return track

    def get_song():
        return input("What Song Would You like to hear? \n>>> ")

    def play_song_in_spotify(spotifyObject):
        deviceID = get_device(spotifyObject)
        trackURI = [_get_track_uri(get_song())]
        spotifyObject.start_playback(deviceID, None, trackURI)
