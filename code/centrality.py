# Implements several definitions of centrality to find the most central song
# of a given graph structure

import sys
import pickle

# defines what the user enters in the console
if len(sys.argv) != 5:
    print "usage: python centrality.py dist.pyfile path.pyfile songlist." + \
        "pyfile [int between 0 and 3]"
    sys.exit()
try:
    option = int(sys.argv[4])
except ValueError:
    print "Please enter an integer!"
    sys.exit()
if option < 0 or option > 3:
    print "Please enter a number between 0 and 3!"
    sys.exit()
        
user_input_1 = sys.argv[1]
user_input_2 = sys.argv[2]
user_input_3 = sys.argv[3]

# imports necessary pyfiles
picklefile = open(user_input_1, 'rb')
dist = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_input_2, 'rb')
path = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_input_3, 'rb')
songlist = pickle.load(picklefile)
picklefile.close()

# Implementation of Bavelas's Closeness Centrality
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

# Implementation of Harmonic Centrality
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

# Implementation of Dangalchev's Centrality
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

# a helper function that generates a list of the songs on the shortest path 
# between two given songs
def generate_path(s1,s2):
    if path[s1][s2] == "null":
        return []
    final_path = [s1]
    while s1 != s2:
        s1 = path[s1][s2]
        final_path.append(s1)
        return final_path

# Implementation of Betweenness Centrality, that calls the helper function
# generate_path
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

# associates each possible entered number with a different type of centrality
if option == 0:
    print "Bavelas's Centrality"
    close_centrality()
elif option == 1:
    print "Harmonic Centrality"
    harmonic_centrality()
elif option == 2:
    print "Dangalchev's Centrality"
    dan_centrality()
else:
    print "Betweeness Centrality"
    between_centrality()