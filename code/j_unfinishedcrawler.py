# crawls playlists, starting from an authenticated user
# returns a list of lists, where the interior lists are all the track IDs
# within each playlist

# address unicodeencodeerror?"

import requests
from requests.exceptions import HTTPError
import sys
import os
import spotipy
import spotipy.util as util
import json

frontier = []
visited = []
output = []

def crawler():
    count = 0
    while len(frontier) > 0 and len(output) < maximum:
        current_user = frontier.pop(0)
        if current_user in visited:
            continue
        else:
            playlists = sp.user_playlists(current_user)
            for playlist in playlists['items']:
                print count
                count += 1
                if len(output) >= maximum:
                    continue
                playlist_owner = playlist['owner']['id']
                if playlist_owner == current_user:
                    try:
                        songs = sp.user_playlist_tracks(playlist_owner, playlist['id'], fields="items")
                    except HTTPError as e:
                        print playlist['id']
                        continue
                    except AttributeError as e: #there is a weird error where some playlist id's are none
                        if playlist['id'] is None:
                            continue
                        else:
                            print playlist['id']
                            raise e
                    new_playlist = []
                    for song in songs['items']:
                        try:
                            new_playlist.append(song['track']['name'])
                        except TypeError as e:
                            continue
#                             if song['track']['name'] is 'NoneType':
#                                 continue
#                             else:
#                                 print song['track']['name']
#                                 raise e
                    output.append(new_playlist)
                    if current_user in visited:
                        continue
                    visited.append(current_user)
                elif "spotify" in playlist_owner:
                    continue
                elif "official" in playlist_owner:
                    continue
                elif "music" in playlist_owner:
                    continue
                elif "spotlight" in playlist_owner:
                    continue
                elif "top" in playlist_owner:
                    continue
                elif "records" in playlist_owner:
                    continue
                elif ".com" in playlist_owner:
                    continue
                elif "games" in playlist_owner:
                    continue
                else:
                    if playlist_owner in visited:
                        continue
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
#        print output[0]
#         with open('playlists.csv', 'wb') as csvfile:
#             outwrite = csv.writer(csvfile)
#             for playlist in output:
#                 outwrite.writerow(playlist)
#         csvfile.close()
#         outfile = open('playlists.pyfile', 'wb')
#         pickle.dump(output, outfile)
#         outfile.close()
        with open('playlists.json', mode = 'w') as f:
            json.dump(output, f)
        print visited
        print len(output)

    else:
        print "Error: Can't get token for", username