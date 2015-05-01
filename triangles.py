# creates a list of triangles, triangles being lists of three songs that
# are all mutually connected with each other

import sys
import pickle

if len(sys.argv) == 3:
    user_input = sys.argv[1]
    song = sys.argv[2]
else:
    print "usage: python triangles.py graph.pyfile 'song'"
    sys.exit()

picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()

output = []
for other_song in user_graph[song]:
    for other_songs_song in user_graph[other_song]:
        if other_songs_song in user_graph[song]:
            output.append([song, other_song, other_songs_song])
return output