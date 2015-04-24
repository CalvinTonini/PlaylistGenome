# An implementation of Floyd-Warshall's algorithm between two nodes
# Input: graph dictionary and two nodes (s1 and s2)
# Output: list of nodes, ordered on the shortest past from s1 to s2

import collections
import sys
import pickle

if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    print "usage: python unfinishedpathfinder.py [graph.csv]"
    sys.exit()

picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()

# sample graph for testing
# testgraph = {
#     'a': {
#         'b': 0.5,
#         'c': 1,
#         'd': 1,
#         },
#     'b': {
#         'a': 0.5,
#         'c': 1
#         },
#     'c': {
#         'a': 1,
#         'b': 1
#         },
#     'd': {
#         'a': 1
#         }
# }

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
    for song in graph:
        songlist.append(song)
    return songlist

# for testing:
# print create_songlist(user_graph)

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
    g = pathfinder(user_graph)
    dist = g.dist
    path = g.path
    if path[songlist.index(s1)][songlist.index(s2)] == "null":
        return []
    final_path = [s1]
    while s1 != s2:
        s1 = path[songlist.index(s1)][songlist.index(s2)]
        final_path.append(s1)
    print final_path

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