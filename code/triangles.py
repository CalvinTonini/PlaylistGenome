# creates a list of triangles, triangles being lists of three songs that
# are all mutually connected with each other

import sys
import pickle

if len(sys.argv) == 6:
    user_input = sys.argv[1]
    song = sys.argv[5]
    user_playlists = sys.argv[2]
    user_dist = sys.argv[3]
    user_songlist = sys.argv[4]
else:
    print "usage: python triangles.py graph.pyfile playlists.pyfile" + \
    " dist.pyfile 'song'"
    sys.exit()

picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_playlists, 'rb')
playlists = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_dist, 'rb')
dist = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_songlist, 'rb')
songlist = pickle.load(picklefile)
picklefile.close()


closeness = []
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
                s_0 = songlist.index(other_songs_song)
                s_1 = songlist.index(song)
                s_2 = songlist.index(other_song)
                c_value = dist[s_0][s_1] + dist[s_1][s_2] + dist[s_2][s_0]
                closeness.append(c_value)
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
# closeness = [0.0] * len(output)
# for i, triangle in enumerate(output):
#     song_0 = triangle[0]
#     song_1 = triangle[1]
#     song_2 = triangle[2]
#     value = dist[song_0][song_1] + dist[song_1][song_2] + dist[song_2][song_0]
#     closeness[i] = value

desired_index = closeness.index(min(closeness))
print desired_index
print output
print closeness