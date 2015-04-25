import collections
import sys
import pickle

if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    print "usage: python printpath.py path.pyfile"
    sys.exit()

picklefile = open(user_input, 'rb')
dist = pickle.load(picklefile)
picklefile.close()

for each in dist:
    print each