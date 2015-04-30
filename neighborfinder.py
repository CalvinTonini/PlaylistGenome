# The "more accurate" version of neighborfinder, based on the dist array

import sys
import pickle

if len(sys.argv) == 5:
    songlist_input = sys.argv[1]
    dist_input = sys.argv[2]
    song_name = sys.argv[3]
    try:
        desired = int(sys.argv[4])
    except ValueError:
        print "please enter an integer!"
        sys.exit()
else:
    print "usage: python neighborfinder.py songlist.pyfile dist.pyfile " \
    + "'song' [number]"
    sys.exit()

picklefile = open(songlist_input, 'rb')
songlist = pickle.load(picklefile)
picklefile.close()
picklefile = open(dist_input, 'rb')
shortest_dist = pickle.load(picklefile)
picklefile.close()

neighbors = []

def neighbor_finder(s,n):
    if s not in songlist:
        print "We don't have that song, sorry!"
        sys.exit()
    while len(neighbors) < n:
        closest = None
        j = songlist.index(s)
        if shortest_dist[j].count(float("inf")) == len(shortest_dist[j]):
            break
        for i, sub_song in enumerate(shortest_dist[j]):
            if closest == None:
                closest = songlist[i]
            elif shortest_dist[j][i] > \
            shortest_dist[j][songlist.index(closest)]:
                continue
            else:
                closest = songlist[i]
        neighbors.append(closest)
        shortest_dist[j][songlist.index(closest)] = float("inf")

neighbor_finder(song_name,desired)
print neighbors
# for debugging
print len(neighbors)

# print shortest_dist[songlist.index("Love On Top")].count(1.0)
# print shortest_dist[songlist.index(song_name)]