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
    if path[songlist.index(s1)][songlist.index(s2)] == "null":
        print "No way to get there."
        return []
    final_path = [s1]
    while s1 != s2:
        s1 = path[songlist.index(s1)][songlist.index(s2)]
        final_path.append(s1)
    print final_path

generate_path(first_song,second_song,user_path)