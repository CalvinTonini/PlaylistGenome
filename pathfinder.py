# An implementation of Floyd-Warshall's algorithm between two nodes
# Input: graph dictionary and two nodes (s1 and s2)
# Output: list of nodes, ordered on the shortest past from s1 to s2

"""Starts with: a weighted graph and two nodes to find the path between them
Return a list of nodes

graph = {
    song: {edge: weight}
    }    
    
graph[song] = {edge: weight}
graph[song][edge] = weight

Structure:
A triple for loop
    For each node a
        Looks at every node b
            And node c
                if the distance from a to b to c is less than the distance from                 a to c directly, update the distance from a to c with the                       distance from a to b to c. Also update the Shortest Path Tree                     that will be returned"""

# sample graph for testing
testgraph = {
    'a': {
        'b': 3,
        'c': 1,
        'd': 1,
        },
    'b': {
        'a': 3,
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

def pathfinder(graph):
    dist = create_dist(graph)
    path = create_path(graph)
    songlist = create_songlist(graph)
    for i, dval in enumerate(dist):
        for j, dval in enumerate(dist):
            if songlist[j] in graph[songlist[i]]:
                dist[i][j] = graph[songlist[i]][songlist[j]]
                path[i][j] = songlist[j]
    print dist
    print path

pathfinder(testgraph)