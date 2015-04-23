# will take a list of lists, where interior lists are playlists, and make a dict 

import sys
import csv

if len(sys.argv) == 2:
    user_input = sys.arg(1)
else:
    print "Sorry, we need a set of playlists to go through"
    sys.exit()

output_graph = {}
current_edge = {}


with open(user_input) as csvfile:
    playlists = []
    insheet = csv.DictReader(csvfile)
    for row in insheet:
        playlists.append(row)

for playlist in playlists:
    for song in playlist:
        if song in output:
            continue
        else:
            for other_song in playlist:
                if other_song == song:
                    continue
                else:
                    current_playlist.append(other_song)
            output["song"] = []
            