# Generates a list of the songs included on the shortest past between two songs
# (if a shortest path exists), based on the matrices created by 
# fasterpathfinder.py.

import sys
import pickle

# defines what the user enters in the console
if len(sys.argv) == 5:
    user_input_1 = sys.argv[1]
    user_input_2 = sys.argv[2]
    first_song = sys.argv[3]
    second_song = sys.argv[4]
else:
    print "usage: python generatepath.py [path.pyfile] [songlist.pyfile] " \
    + "[song_1] [song_2]"
    sys.exit()

# imports necessary pyfiles
picklefile = open(user_input_1, 'rb')
user_path = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_input_2, 'rb')
songlist = pickle.load(picklefile)
picklefile.close()

# Looks at the relevant cells in the shortest path matrix to construct a list
# containing the songs located on the shortest path between two songs.
def generate_path(s1,s2,path):
    song_1 = songlist.index(s1)
    song_2 = songlist.index(s2)
    if path[song_1][song_2] == "null":
        print "Sorry, these songs aren't connected."
        return []
    final_path = [s1]
    while song_1 != song_2:
        song_1 = path[song_1][song_2]
        final_path.append(songlist[song_1])
    print final_path

generate_path(first_song,second_song,user_path)