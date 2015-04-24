import sys
import pickle

if len(sys.argv) == 3:
    dist = sys.argv[1]
    path = sys.argv[2]
else:
    print "usage: python unfinishedcentralcalc.py [dist.py] [path.py]"
    sys.exit()

centrality = [0.0] * len(dist)

songlist = []
for song in graph:
    songlist.append(song)

for value in centrality:
    for i, song in enumerate(graph):
        for edge in dist[song]:
            value += dist[song][edge]
        
