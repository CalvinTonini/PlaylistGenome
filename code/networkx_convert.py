# Allows us to visualize the graph structure

import networkx as nx
import sys
import collections
import pickle
import matplotlib.pyplot as plt

# defines what the user enters in the console
if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    print "usage: python networkx_convert.py [graph.pyfile]"
    sys.exit()

# imports pyfiles
picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()

# uses the weights of the edges to draw the graph
G=nx.Graph()
G.add_nodes_from(user_graph)
for song, edges in user_graph.iteritems():
    for other_song, weight in edges.iteritems():
        G.add_weighted_edges_from([(song, other_song, weight)])
nx.draw(G)
plt.show()
