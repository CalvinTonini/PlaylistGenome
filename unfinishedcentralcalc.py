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

for value in centrality:
    for i, song in enumerate(dist):
        new_value = 0.0
        for j, edge in enumerate(dist[i]):
            new_value = new_value + dist[i][j]
        centrality[i] = (1.0/new_value)

thing = centrality.index(max(centrality))
print songlist[thing]