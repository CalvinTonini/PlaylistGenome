# Finds the song with the highest Betweeness Centrality given multiple songs

import sys
import pickle

# defines what the user enters in the console
if len(sys.argv) != 3:
    print "usage: python playlistneighborfinder.py path.pyfile songlist.pyfile"
    sys.exit()
user_input_1 = sys.argv[1]
user_input_2 = sys.argv[2]

# imports necessary pyfiles
picklefile = open(user_input_1, 'rb')
path = pickle.load(picklefile)
picklefile.close()
picklefile = open(user_input_2, 'rb')
songlist = pickle.load(picklefile)
picklefile.close()

# Prompts that guide the user to enter song names
song_list = []
limit = True
while limit:
    s = raw_input("Give me some songs you have on a playlist together: ")
    if s not in songlist:
        print "We don't have that song."
    else:
        song_list.append(s)
    answer = ""
    while answer != "y" and answer != "n":
        answer = raw_input("Do you want to add another song? y or n: ")
        if answer != "y" and answer != "n":
            print "Please type in y or n!"
        if answer == "n":
            limit = False

# a helper function that generates a list of songs on the shortest path
# between two songs (taken from generatepath.py)
def generate_path(s1,s2):
    if path[s1][s2] == "null":
        return []
    final_path = [s1]
    while s1 != s2:
        s1 = path[s1][s2]
        final_path.append(s1)
        return final_path

# An implementation of Betweenness Centrality that finds the most traversed 
# song on the shortest path between the entered songs and every other song 
# (modified from centrality.py)
def between_centrality():
    centrality = [0.0] * len(path)
    for i, song in enumerate(path):
        value = 0.0
        for j, node_1 in enumerate(path):
            if i == j:
                continue
            for k, node_2 in enumerate(song_list):
                if i == k:
                    continue
                if i in generate_path(j,k):
                    value += 1
        centrality[i] = value/(len(path)**2)
    thing = centrality.index(max(centrality))
    print songlist[thing]

between_centrality()