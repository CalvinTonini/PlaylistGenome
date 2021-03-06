# An implementation of Floyd-Warshall's algorithm that also attempts to improve 
# the running time of pathfinder.py by taking advantage of the fact that the 
# distance matrix is symmetric in undirected graphs, updating both halves of 
# the matrix at the same time.

import sys
import pickle

# defines what the user enters in the console
if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    print "usage: python unfinishedfasterpathfinder.py [graph.pyfile]"
    sys.exit()

# imports necessary pyfiles
picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()

# a helper function that creates a songlist given a graph
def create_songlist(graph):
    songlist = []
    for song in graph:
        songlist.append(song)
    return songlist

# a helper function that creates a shortest matrix given a graph
def create_path(graph):
    path = []
    for i in range(len(graph)):
        path.append(["null"] * (len(graph)))
    return path

# a helper function that creates a distance matrix given a graph
def create_dist(graph):
    dist = []
    for i in range(len(graph)):
        dist.append([float("inf")] * (len(graph)))
    return dist

# looks at only /unique/ song pairs in the graph and updates the distance and
# path matrices with the appropriate weights and songs (respectively)
def pathfinder(graph):
    songlist = create_songlist(user_graph)
    dist = create_dist(graph)
    path = create_path(graph)
    for i in xrange(len(graph) - 1):
        for j in xrange(len(graph) - i - 1):
            j_actual = (j + i + 1)
            if songlist[j_actual] in graph[songlist[i]]:
                dist[i][j_actual] = graph[songlist[i]][songlist[j_actual]]
                dist[j_actual][i] = graph[songlist[i]][songlist[j_actual]]
                path[i][j_actual] = j_actual
                path[j_actual][i] = i
    for i in xrange(len(graph) - 1):
        for j in xrange(len(graph) - i - 1):
            j_actual = (j + i + 1)
            if j_actual == i:
                continue
            for k in xrange(len(graph) - 1):
                if k == i or k == j_actual:
                    continue
                j_actual = (j + i + 1)
                if dist[i][k] + dist[k][j_actual] < dist[i][j_actual]:
                    dist[i][j_actual] = dist[i][k] + dist[k][j_actual]
                    dist[j_actual][i] = dist[i][k] + dist[k][j_actual]
                    path[i][j_actual] = path[i][k]
                    path[j_actual][i] = path[j_actual][k]

    output_file = open('dist_fast.pyfile', 'wb')
    pickle.dump(dist, output_file)
    output_file.close()
    output_file = open('path_fast.pyfile','wb')
    pickle.dump(path, output_file)
    output_file.close()
    output_file = open('songlist_fast.pyfile', 'wb')
    pickle.dump(songlist, output_file)
    output_file.close()

pathfinder(user_graph)