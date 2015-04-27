from igraph import *

import sys
import csv
import json
import pickle

if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    print "usage: python convert.py graph.pyfile"
    sys.exit()

picklefile = open(user_input, 'rb')
user_graph = pickle.load(picklefile)
picklefile.close()

def create_songlist(graph):
    songlist = []
    for song in graph:
        songlist.append(song)
    return songlist

songlist = create_songlist(user_graph)

output = Graph()
output.add_vertices(len(user_graph))
count = 0
value = []
for i, node in enumerate(songlist):
    output.vs[i]["title"] = node
    for song in user_graph[node]:
        if i > songlist.index(song):
            continue
        output.add_edges([(i, (songlist.index(song)))])
        output.es[int(count)]["weight"] = user_graph[node][song]
        count += 1

visual_style = {}
visual_style["edge_width"] = [1 + 2 * weight for weight in output.es["weight"]]
visual_style["vertex_label"] = output.vs["title"]
plot(output, **visual_style)
