import collections
import sys
import pickle

if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    print "usage: python printsong.py songlist.pyfile"
    sys.exit()

picklefile = open(user_input, 'rb')
song = pickle.load(picklefile)
picklefile.close()

for each in song:
    print each