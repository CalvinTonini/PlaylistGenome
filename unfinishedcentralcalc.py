import sys
import pickle

picklefile = open("dist.pyfile", 'rb')
dist = pickle.load(picklefile)
picklefile.close()
picklefile = open("path.pyfile", 'rb')
path = pickle.load(picklefile)
picklefile.close()
picklefile = open("songlist.pyfile", 'rb')
songlist = pickle.load(picklefile)
picklefile.close()

if len(sys.argv) != 4:
    print "usage: python unfinishedcentralcalc.py dist.pyfile path.pyfile songlist.pyfile"
    sys.exit()

def close_centrality_0():
    centrality = [0.0] * len(dist)
    for i, song in enumerate(dist):
        new_value = 0.0
        for j, edge in enumerate(dist[i]):
            if dist[i][j] == float("inf"):
                continue
            else:
                new_value += (dist[i][j])
        centrality[i] = (1/new_value)
    thing = centrality.index(max(centrality))
    print songlist[thing]

def close_centrality_1():
    centrality = [0.0] * len(dist)
    for i, song in enumerate(dist):
        new_value = 0.0
        for j, edge in enumerate(dist[i]):
            if dist[i][j] == float("inf"):
                continue
            else:
                new_value += 1/(dist[i][j])
        centrality[i] = new_value
    thing = centrality.index(max(centrality))
    print songlist[thing]

def close_centrality_2():
    centrality = [0.0] * len(dist)
    for i, song in enumerate(dist):
        new_value = 0.0
        for j, edge in enumerate(dist[i]):
            if dist[i][j] == float("inf"):
                continue
            else:
                new_value += 1/(2**dist[i][j])
        centrality[i] = new_value
    thing = centrality.index(max(centrality))
    print songlist[thing]


def generate_path_1(s1,s2):
    if path[songlist.index(s1)][songlist.index(s2)] == "null":
        return []
    final_path = [s1]
    while s1 != s2:
        s1 = path[songlist.index(s1)][songlist.index(s2)]
        final_path.append(s1)
        return final_path
    
def between_centrality():
    centrality = [0.0] * len(path)
    for i, song in enumerate(path):
        value = 0.0
        for j, node_1 in enumerate(path):
            if i == j:
                continue
            for k, node_2 in enumerate(path):
                if i == k:
                    continue
                if song in generate_path_1(node_1,node_2):
                    value += 1
        centrality[i] = value/(len(dist)**2)
    thing = centrality.index(max(centrality))
    print songlist[thing]


between_centrality()