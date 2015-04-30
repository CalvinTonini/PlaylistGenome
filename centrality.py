import sys
import pickle

if len(sys.argv) != 4:
    print "usage: python centrality.py dist.pyfile path.pyfile songlist.pyfile"
    sys.exit()
user_input_1 = sys.argv[1]
user_input_2 = sys.argv[2]
user_input_3 = sys.argv[3]

picklefile = open(user_input_1, 'rb')
dist = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_input_2, 'rb')
path = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_input_3, 'rb')
songlist = pickle.load(picklefile)
picklefile.close()

# Basic closeness centrality, based off Bavelas's definition of closeness,
# (i.e. closeness is the reciprocal of farness)
# Not the best definition to use
def close_centrality():
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

# harmonic centrality: natural modification of Bavelas's definition.
# useful for when a graph is not strongly connected (Rochat 2009)
def harmonic_centrality():
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

# Dangalchev's (2006) definition of centrality
def dan_centrality():
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

# a helper function for between_centrality
def generate_path(s1,s2):
    if path[s1][s2] == "null":
        return []
    final_path = [s1]
    while s1 != s2:
        s1 = path[s1][s2]
        final_path.append(s1)
        return final_path

# betweenness centrality: quantifies the number of times a node acts as a 
# bridge along the shortest path between two nodes
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
                if i in generate_path(j,k):
                    value += 1
        centrality[i] = value/(len(dist)**2)
    thing = centrality.index(max(centrality))
    print songlist[thing]

# call centrality functions here
close_centrality()
harmonic_centrality()
dan_centrality()
between_centrality()