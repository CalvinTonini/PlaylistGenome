# crawls playlists
# returns a list of lists, where the interior lists are all the track IDs
# within each playlist

import sys
import os
import spotipy
import spotipy.util as util
import json

frontier = []
visited = []
output = []

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
                    songs = sp.user_playlist(playlist_owner, playlist['id'], fields="tracks,next")
                    new_playlist = []
                    for song in songs['tracks']['items']:
                        new_playlist.append(song['track']['name'])
                    output.append(new_playlist)
                    visited.append(current_user)
                elif playlist_owner != 'spotify':
                    if playlist_owner in visited:
                        continue
                    else:
                        frontier.append(playlist_owner)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        username = sys.argv[1]
        try: 
            maximum = int(sys.argv[2])
        except ValueError:
            print "please enter an integer!"
            sys.exit()
    else:
        print "usage: python unfinishedcrawler.py [username] [number]"
        sys.exit()

    token = util.prompt_for_user_token(username)

    if token:
        frontier.append(username)
        sp = spotipy.Spotify(auth=token)
        crawler()
        print output
    else:
        print "Can't get token for", username
