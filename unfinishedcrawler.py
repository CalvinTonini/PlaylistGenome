# Crawls Playlists, starting from an authenticated user.

import sys
import os
import spotipy
import spotipy.util as util
import json

frontier = []
visited = []
output = []
# maximum number of playlists, checked when starting a new user
maximum = 50

def crawler():
    while len(frontier) > 0 and len(output) < maximum :
        current_user = frontier.pop()
        if current_user in visited:
            continue
        else:
            playlists = sp.user_playlists(current_user)
            for playlist in playlists['items']:
                playlist_owner = playlist['owner']['id']
                if playlist_owner == current_user:
                    songs = sp.user_playlist(playlist_owner, playlist['id'], fields="tracks")
                    new_playlist = []
                    for song in songs['tracks']['items']:
                        new_playlist.append(song['track']['id'])
                    output.append(new_playlist)
                    if current_user in visited:
                        continue
                    visited.append(current_user)
                elif playlist_owner != 'spotify':
                    if playlist_owner in visited:
                        continue
                    frontier.append(playlist_owner)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print "usage: python unfinishedcrawler.py [username]"
        sys.exit()

    token = util.prompt_for_user_token(username)

    if token:
        frontier.append(username)
        sp = spotipy.Spotify(auth=token)
        crawler()
        print output
    else:
        print "Error: Can't get token for", username