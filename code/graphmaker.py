# constructs a graph structure from data generated by crawler.py

import sys
import csv
import pickle

def graphmaker():
    # defines what the user enters in the console
    if len(sys.argv) == 2:
        user_input = sys.argv[1]
    else:
        print "usage: python graphmaker.py [playlists.pyfile]"
        sys.exit()
    output_graph = {}
    current_edge = {}
    picklefile = open(user_input, 'rb')
    playlists = pickle.load(picklefile)
    picklefile.close()
    # responsible for calculating and assigning node weights
    for playlist in playlists:
        playlist = set(playlist)
        for song in playlist:
            if song in output_graph:
                for other_song in playlist:
                    if other_song == song:
                        continue
                    elif other_song in output_graph[song]:
                        new_v = output_graph[song][other_song]
                        new_v = (1.0/new_v) + 1
                        new_v = 1.0/new_v
                        output_graph[song][other_song] = new_v
                    else:
                        output_graph[song][other_song] = 1.0
            else:
                output_graph[song] = {}
                for other_song in playlist:
                    if other_song == song:
                        continue
                    else:
                        output_graph[song][other_song] = 1.0
    output_file = open('graph.pyfile', 'wb')
    pickle.dump(output_graph, output_file)
    output_file.close()

graphmaker()