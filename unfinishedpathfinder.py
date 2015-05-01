# An implementation of Floyd-Warshall's algorithm between two nodes
# Input: graph dictionary and two nodes (s1 and s2)
# Output: list of nodes, ordered on the shortest past from s1 to s2

import collections
import sys
import pickle

if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    print "usage: python unfinishedpathfinder.py graph.pyfile"
    sys.exit()

picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()

# sample graph for testing
# user_graph = {
#     'a': {
#         'b': 0.1,
#         'c': .21,
#         'd': .301,
#         },
#     'b': {
#         'a': 0.1,
#         'c': .4001,
#         'd': 1
#         },
#     'c': {
#         'a': .21,
#         'b': .4001
#         },
#     'd': {
#         'a': .301,
#         'b': 1
#         }
#     }

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

songlist = create_songlist(user_graph)
h = pathfinder(user_graph)
h1 = h.dist
h2 = h.path

output_file = open('dist0.pyfile', 'wb')
pickle.dump(h1, output_file)
output_file.close()
output_file = open('path0.pyfile','wb')
pickle.dump(h2, output_file)
output_file.close()
output_file = open('songlist0.pyfile','wb')
pickle.dump(songlist, output_file)
output_file.close()