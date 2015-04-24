import sys
import pickle

picklefile = open("dist.pyfile", 'rb')
dist = pickle.load(picklefile)
picklefile.close()
picklefile = open("songlist.pyfile", 'rb')
songlist = pickle.load(picklefile)
picklefile.close()


if len(sys.argv) != 3:
    print "usage: python unfinishedcentralcalc.py dist.pyfile songlist.pyfile"
    sys.exit()

centrality = [0.0] * len(dist)

for i, song in enumerate(dist):
    new_value = 0.0
    for j, edge in enumerate(dist[i]):
        if dist[i][j] == float("inf"):
            continue
        else:
            new_value = new_value + dist[i][j]
    centrality[i] = (1.0/new_value)
print songlist
print centrality
thing = centrality.index(max(centrality))
print songlist[thing]