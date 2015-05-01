# An implementation of Floyd-Warshall's algorithm between two nodes

import collections
import sys
import pickle

# defines what the user enters in the console
if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    print "usage: python unfinishedpathfinder.py graph.pyfile"
    sys.exit()

# imports necessary pyfiles
picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()

# a helper function that creates a distance matrix given a graph
def create_dist(graph):
    dist = []
    for i in range(len(graph)):
        dist.append([float("inf")] * (len(graph)))
    return dist

# a helper function that creates a shortest path matrix given a graph
def create_path(graph):
    path = []
    for i in range(len(graph)):
        path.append(["null"] * (len(graph)))
    return path

# a helper function that creates a songlist given a graph
def create_songlist(graph):
    songlist = []
    for song in graph:
        songlist.append(song)
    return songlist

# traverses the graph and updates the distance and path matrices with the 
# appropriate weights and songs (respectively)
def pathfinder(graph):
    dist = create_dist(graph)
    path = create_path(graph)
    for i, d_i in enumerate(dist):
        for j, d_j in enumerate(dist):
            if songlist[j] in graph[songlist[i]]:
                dist[i][j] = graph[songlist[i]][songlist[j]]
                path[i][j] = j
    for i, d_i in enumerate(dist):
        for j, d_j in enumerate(dist):
            for k, d_k in enumerate(dist):
                if i == k or j == k or i == j:
                    continue
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = (dist[i][k] + dist[k][j])
                    path[i][j] = path[i][k]
    finder = collections.namedtuple('finder',['dist','path'])
    f = finder(dist,path)
    return f

# splits the output so that it can be saved as separate pyfiles
songlist = create_songlist(user_graph)
h = pathfinder(user_graph)
h1 = h.dist
h2 = h.path

output_file = open('dist.pyfile', 'wb')
pickle.dump(h1, output_file)
output_file.close()
output_file = open('path.pyfile','wb')
pickle.dump(h2, output_file)
output_file.close()
output_file = open('songlist.pyfile','wb')
pickle.dump(songlist, output_file)
output_file.close()