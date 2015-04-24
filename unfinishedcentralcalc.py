import sys
import pickle

picklefile = open("path.pyfile", 'rb')
f = pickle.load(picklefile)
picklefile.close()

if len(sys.argv) != 1:
    print "usage: python unfinishedcentralcalc.py [dist.py] [path.py]"
    sys.exit()

centrality = [0.0] * len(dist)

songlist = []
for song in f.dist:
    songlist.append(song)

for value in centrality:
    for i, song in enumerate(f.dist):
        for edge in f.dist[song]:
            value += f.dist[song][edge]

print max(centrality)