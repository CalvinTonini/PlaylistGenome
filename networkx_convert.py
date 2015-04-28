import networkx as nx
import sys
import collections
import pickle
import matplotlib.pyplot as plt

if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    print "usage: python networkx_convert.py [graph.pyfile]"
    sys.exit()

picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()

# Do the thing! Score the points!
G=nx.Graph()
G.add_nodes_from(user_graph)
for song, edges in user_graph.iteritems():
    for other_song, weight in edges.iteritems():
        G.add_weighted_edges_from([(song, other_song, weight)])
# print G.nodes()
# print G.edges()
# for n,nbrs in G.adjacency_iter():
#     for nbr,eattr in nbrs.items():
#         data=eattr['weight']
#         print('(%s, %s, %.3f)' % (n,nbr,data))
nx.draw(G)
plt.show()
