# utilizes spotipy, developed by Plamere, available at 
# https://github.com/plamere/spotipy
# to install, type in command-line: pip install spotipy

import pprint
import sys
import os
import subprocess

import spotipy

# potentially useful spotipy features?
# client Module
user_playlist_tracks(user, playlistid, fields, limit=100, offset=0)
user_playlists(user, limit=50, offset=0) 
# oauth2 Module
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
get_access_token(code)
# util Module
spotipy.util.prompt_for_user_token(username, scope=None, client_id=None, client_secret=None, redirect_uri=None)

# 1. user -> get all their playlists
# 2.     if spotify playlist -> leave alone
# 3.     if user playlist -> get playlist and all tracks, and move to next playlist
# 4.     if other -> take data, and store that username on frontier

# given one user account, search through their public playlists for new 
# usernames
user = 

def get_users(user)

# calls find_users, and goes through the ids to gather playlist data
def gather_playlists(user)

# calls gather_playlists, runs until while loop conditions are fulfilled,
# i.e. we reach our database goal or there are no more usernames to go through
def crawler(user):
    while data limit reached and frontier not empty