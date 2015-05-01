import collections
import sys
import pickle

if len(sys.argv) == 3:
    user_input_0 = sys.argv[1]
    user_input_1 = sys.argv[2]
else:
    print "usage: python printpath.py path.pyfile songlist.pyfile"
    sys.exit()

picklefile = open(user_input_0, 'rb')
path = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_input_1, 'rb')
songlist = pickle.load(picklefile)
picklefile.close()

for i, each in enumerate(path):
    for j, song in enumerate(path[i]):
        if path[i][j] == "null":
            continue
        path[i][j] = songlist[path[i][j]]

for i, each in enumerate(path):
    print path[i]