import collections
import sys
import pickle

if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    print "usage: python unfinishedpathfinder.py [graph.pyfile]"
    sys.exit()

picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()

for each in user_graph[750]:
    print each