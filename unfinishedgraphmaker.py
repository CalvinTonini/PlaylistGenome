# will take a list of lists, where interior lists are playlists, and make a dict 

import sys

if len(sys.argv) == 2:
    user_input = sys.argv(1)
else:
    print "Sorry, we need a set of playlists to go through"
    sys.exit()

output_graph = {}
current_edge = {}

for playlist in user_input:
    for song in playlist:
        if song in output:
            continue
        else:
            output_graph[song] = {}
            for other_song in playlist:
                if other_song == song:
                    continue
                else:
                    output_graph[song][other_song]= 1