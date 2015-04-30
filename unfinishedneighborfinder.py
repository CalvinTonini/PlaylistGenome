# input: graph, reference to a specific node
# output: list of nearby nodes (int unput to determine number, e.g. top 10)

"""BUG: figure out how to tell users they've entered a song title we don't have. Also, it's not working for King of Anything?"""

import collections
import sys
import pickle

if len(sys.argv) == 4:
    user_input = sys.argv[1]
    song_name = sys.argv[2]
    try:
        maximum = int(sys.argv[3])
    except ValueError:
        print "please enter an integer!"
        sys.exit()
else:
    print "usage: python unfinishedneighborfinder.py graph.pyfile 'song' [number]"
    sys.exit()

picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()

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

# print len(user_graph["a"])

# def test(s,n):
#     tests = []
#     while len(tests) < n and len(tests) != len(user_graph[s]):
#         for song in user_graph[s]:
#             tests.append(song)
#             print tests

# test(song_name,maximum)

# simple implementation: take a node, compare every weight against each other, returning the top x nodes with the highest edge weight values
def neighbor_finder(s,n):
    neighbors = []
    while len(neighbors) < n:
        closest = None
        if len(user_graph[s]) == 0:
                return neighbors
                sys.exit()
        for sub_song in user_graph[s]:
            if closest == None:
                closest = sub_song
            elif user_graph[s][sub_song] > user_graph[s][closest]:
                continue
            else:
                closest = sub_song
        neighbors.append(closest)
        del user_graph[s][closest]
    return neighbors
print neighbor_finder(song_name,maximum)
