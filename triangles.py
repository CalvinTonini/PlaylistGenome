# creates a list of triangles, triangles being lists of three songs that
# are all mutually connected with each other

import sys
import pickle

if len(sys.argv) == 4:
    user_input = sys.argv[1]
    song = sys.argv[3]
    user_playlists = sys.argv[2]
else:
    print "usage: python triangles.py graph.pyfile playlists.pyfile 'song'"
    sys.exit()

picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_playlists, 'rb')
playlists = pickle.load(picklefile)
picklefile.close()

output = set()
for other_song in user_graph[song]:
    for other_songs_song in user_graph[other_song]:
        if other_songs_song in user_graph[song]:
            triangle = frozenset([other_songs_song, song, other_song])
            flag = False
            for playlist in playlists:
                if triangle.issubset(set(playlist)):
                    flag = True
            if flag == False:
                output.add(triangle)
# for song in user_graph:
#     for other_song in user_graph[song]:
#         for other_songs_song in user_graph[other_song]:
#             if other_songs_song in user_graph[song]:
#                 triangle = frozenset([other_songs_song, song, other_song])
#                 flag = False
#                 for playlist in playlists:
#                     if triangle.issubset(set(playlist)):
#                         flag = True
#                 if flag == False:
#                     output.add(triangle)
print output