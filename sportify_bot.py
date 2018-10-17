import os
import sys
import json

import spotipy
import webbrowser
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
# from json.decoder import JSONDecodeError

# get the username from the terminal
username = 'xxmyp4fglpr2bry8o91266vx8'

# user id: https://open.spotify.com/user/xxmyp4fglpr2bry8o91266vx8?si=SRebMAO5S4WszSd90PRWDw

# Erase cache and prompt for user permission

token = util.prompt_for_user_token(username, scope='streaming', client_id='66991a05186c41e79b6621d794ffaabb', client_secret="847a0ff59a39484882ddfa6087e24a5a", redirect_uri="http://www.google.com/")

# create spotify object

spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

displayName = user['display_name']
followers = user['followers']['total']

while True:
    print()
    print(">>> Welcome to Spotipy {}!".format(displayName))
    print(">>> You have {} followers\n".format(followers))
    print("0 - Search for an artist")
    print("1 - Exit")
    print("2 - Search a Song")
    choice = int(input("Your coice: "))
    if choice == 0:
        searchQuery = input("Ok, what's their name?: ")

        # dictionary  from query
        searchResults = spotifyObject.search(searchQuery, limit=1, type='artist')

        # get album art
        webbrowser.open(searchResults['artists']['items'][0]['images'][0]['url'])
    if choice == 2:
        searchQuery = input("song name: ")

        resp = spotifyObject.search(searchQuery, limit=1, offset=0, type='track', market='US')
        # print track details
        trackURI = resp['tracks']['items'][0]['uri']
        print(trackURI)
    else:
        break
# print(json.dumps(VARIABLE, sort_keys=True, indent=4))




