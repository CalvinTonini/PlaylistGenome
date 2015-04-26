import sys
import pickle

if len(sys.argv) == 5:
    first_song = sys.argv[1]
    second_song = sys.argv[2]
    user_input_1 = sys.argv[3]
    user_input_2 = sys.argv[4]
else:
    print "usage: python unfinishedpathfinder.py first_song second_song path.pyfile songlist.pyfile"
    sys.exit()

picklefile = open(user_input_1, 'rb')
user_path = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_input_2, 'rb')
songlist = pickle.load(picklefile)
picklefile.close()

def generate_path(s1,s2,path):
    song_1 = songlist.index(s1)
    song_2 = songlist.index(s2)
    if path[song_1][song_2] == "null":
        print "No way to get there."
        return []
    final_path = [s1]
    while song_1 != song_2:
        song_1 = path[song_1][song_2]
        final_path.append(songlist[song_1])
    print final_path

generate_path(first_song,second_song,user_path)