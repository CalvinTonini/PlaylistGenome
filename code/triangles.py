# Creates a list of "triangles," i.e. lists of three songs that
# are all mutually connected (but not on the same playlist) with each other.
# Given a song, triangles.py will return the closest triangle containing
# that song.

import sys
import pickle


# defines what the user enters in the console
if len(sys.argv) == 6:
    user_input = sys.argv[1]
    song = sys.argv[5]
    user_playlists = sys.argv[2]
    user_dist = sys.argv[3]
    user_songlist = sys.argv[4]
else:
    print "usage: python triangles.py graph.pyfile playlists.pyfile" + \
    " dist.pyfile songlist.pyfile 'song'"
    sys.exit()

# imports necessary pyfiles
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
real_output = []
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
                real_output.append([song, other_song, other_songs_song])
if real_output == []:
    print "Sorry, No Triangles"
    sys.exit()
desired_index = closeness.index(min(closeness))
print real_output[desired_index]