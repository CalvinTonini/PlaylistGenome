# An implementation of Floyd-Warshall's algorithm between two nodes
# Input: graph dictionary and two nodes (s1 and s2)
# Output: list of nodes, ordered on the shortest past from s1 to s2 BUT will only output half a matrix

import cProfile

# import collections
import sys
import pickle

if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    print "usage: python unfinishedpathfinder.py [graph.pyfile]"
    sys.exit()

dist = []
path = []
songlist = []

picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()
# picklefile = open(user_input_1, 'rb')
# songlist = pickle.load(picklefile)
# picklefile.close()

# user_input_1 = sys.argv[1]
# picklefile = open(user_input_1, 'rb')
# songlist = pickle.load(picklefile)
# picklefile.close()

# sample graph for testing
# user_graph = {
#     'a': {
#         'b': 0.5,
#         'c': 1,
#         'd': 1,
#         },
#     'b': {
#         'a': 0.5,
#         'c': .25,
#         'd': 2
#         },
#     'c': {
#         'a': 1,
#         'b': .25
#         },
#     'd': {
#         'a': 1,
#         'b': 2
#         }
#     }

def create_songlist(graph):
    songlist = []
    for song in graph:
        songlist.append(song)
    return songlist

def create_dist(graph):
    dist = []
    for i in range((len(graph))-1):
        dist.append([float("inf")] * (((len(graph)) - 1) - i))
    return dist

def create_path(graph):
    path = []
    for i in range(len(graph)):
        path.append(["null"] * (len(graph)))
    return path

def create_output_dist(graph):
    dist = []
    for i in range(len(graph)):
        dist.append([float("inf")] * (len(graph)))
    return dist

# for testing:
# print create_songlist(user_graph)

def pathfinder(graph):
    global songlist, dist, path
    songlist = create_songlist(user_graph)
    dist = create_output_dist(graph)
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
#                 j_actual = (j + i + 1)
#                 k_i = (k - i - 1)
#                 k_j = (k - j_actual - 1)
#                 i_k = (i - k - 1)
#                 i_j = (i - j_actual - 1)
#                 j_k = (j_actual - k - 1)
#                 if k == i or k == j_actual:
#                     continue
#                 if k > i: # k first
#                     if k > j_actual: # k first and use k_v
#                         if dist[i][k_i] + dist[j_actual][k_j] < dist[i][j]:
#                             dist[i][j] = dist[i][k_i] + dist[j_actual][k_j]
#                             path[i][j] = path[i][k_i]
#                         continue
#                     if dist[i][k_i] + dist[k][j_k] < dist[i][j]:
#                         dist[i][j] = dist[i][k_i] + dist[k][j_k]
#                         path[i][j] = path[i][k_i]
#                     continue
#                 if k > j_actual:
#                     if dist[k][i_k] + dist[j_actual][k_j] < dist[i][j]:
#                         dist[i][j] = dist[k][i_k] + dist[j_actual][k_j]
#                         path[i][j] = path[k][i_k]
#                     continue
#                 if dist[k][i_k] + dist[k][j_k] < dist[i][j]:
#                     dist[i][j] = dist[k][i_k] + dist[k][j_k]
#                     path[i][j] = path[k][i_k]
#     finder = collections.namedtuple('finder',['dist','path'])
#     f = finder(dist,path)
#     return f


# h = pathfinder(user_graph)
# h1 = h.dist
# h2 = h.path

    output_file = open('dist.pyfile', 'wb')
    pickle.dump(dist, output_file)
    output_file.close()
    output_file = open('path.pyfile','wb')
    pickle.dump(path, output_file)
    output_file.close()
    output_file = open('songlist.pyfile', 'wb')
    pickle.dump(songlist, output_file)
    output_file.close()

cProfile.run("pathfinder(user_graph)")