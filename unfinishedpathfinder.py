# An implementation of Floyd-Warshall's algorithm between two nodes
# Input: graph dictionary and two nodes (s1 and s2)
# Output: list of nodes, ordered on the shortest past from s1 to s2

# sample graph for testing

import collections
import sys

#if len(sys.argv) == 2:
#    user_input = sys.argv[1]
#else:
#    print "usage: python unfinishedpathfinder.py [graph.csv]"
#    sys.exit()

testgraph = {
    'a': {
        'b': 0.5,
        'c': 1,
        'd': 1,
        },
    'b': {
        'a': 0.5,
        'c': 1
        },
    'c': {
        'a': 1,
        'b': 1
        },
    'd': {
        'a': 1
        }    
}

def create_dist(graph):
    dist = []
    for i in range(len(graph)):
        dist.append([float("inf")] * (len(graph)))
    return dist

def create_path(graph):
    path = []
    for i in range(len(graph)):
        path.append(["null"] * (len(graph)))
    return path

def create_songlist(graph):
    songlist = []
    for song in testgraph:
        songlist.append(song)
    return songlist

# for testing
print create_songlist(testgraph)
songlist = create_songlist(testgraph)

def pathfinder(graph):
    dist = create_dist(graph)
    path = create_path(graph)
    for i, d_i in enumerate(dist):
        for j, d_j in enumerate(dist):
            if songlist[j] in graph[songlist[i]]:
                dist[i][j] = graph[songlist[i]][songlist[j]]
                path[i][j] = songlist[j]
    for i, d_i in enumerate(dist):
        for j, d_j in enumerate(dist):
            for k, d_k in enumerate(dist):
                if i == j or i == k or j == k:
                    continue
                if dist[i][j] + dist[j][k] < dist[i][k]:
                    dist[i][k] = dist[i][j] + dist[j][k]
                    path[i][k] = path[i][j]
    finder = collections.namedtuple('finder',['dist','path'])
    f = finder(dist,path)
    return f

def generate_path(s1,s2):
    g = pathfinder(graph)
    dist = g.dist
    path = g.path
    if path[songlist.index(s1)][songlist.index(s2)] == "null":
        return []
    final_path = [s1]
    while songlist[i] != songlist[j]:
        songlist[i] = path[i][j]
        final_path.append[songlist[i]]
    return final_path

pathfinder(testgraph)