# An implementation of neighbor_finder that uses
# hoursonglist.pyfile and hourdist.pyfile to compare results with the basic 
# neighbor_finder.

import sys
import pickle

if len(sys.argv) == 5:
    songlist_input = sys.argv[1]
    dist_input = sys.argv[2]
    song_name = sys.argv[3]
    try:
        maximum = int(sys.argv[4])
    except ValueError:
        print "please enter an integer!"
        sys.exit()
else:
    print "usage: python unfinishedneighborfinder.py songlist.pyfile dist.pyfile 'song' [number]"
    sys.exit()

picklefile = open(songlist_input, 'rb')
songlist = pickle.load(picklefile)
picklefile.close()
picklefile = open(dist_input, 'rb')
shortest_dist = pickle.load(picklefile)
picklefile.close()

def neighbor_finder(s,n):
    if s not in songlist:
        print "We don't have that song, sorry!"
        sys.exit()
    neighbors = []
    while len(neighbors) < n:
        closest = None
        j = songlist.index(s)
        if all( i is float("inf") for i in shortest_dist[j] ):
                return neighbors
                sys.exit()
        for i, sub_song in enumerate(shortest_dist[j]):
            if closest == None:
                closest = songlist[i]
            elif shortest_dist[j][i] > shortest_dist[j][songlist.index(closest)]:
                continue
            else:
                closest = songlist[i]
        neighbors.append(closest)
        shortest_dist[j][songlist.index(closest)] = float("inf")
    return neighbors
        
print neighbor_finder(song_name,maximum)