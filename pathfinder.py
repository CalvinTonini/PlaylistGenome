# An implementation of Floyd-Warshall's algorithm between two nodes
# Input: graph dictionary and two nodes (s1 and s2)
# Output: list of nodes, ordered on the shortest past from s1 to s2

"""Starts with: a weighted graph and two nodes to find the path between them
Return a list of nodes

graph = {
    song: {edges: weights}
    }    
    
graph[song] = {edges: weights}
graph[song][edges] = weights

Structure:
A triple for loop
    For each node a
        Looks at every node b
            And node c
                if the distance from a to b to c is less than the distance from                 a to c directly, update the distance from a to c with the                       distance from a to b to c. Also update the Shortest Path Tree                     that will be returned"""

testgraph = {
    'a': {
        'b': 3,
        'c': 1
        },
    'b': {
        'a': 3,
        'c': 1
        },
    'c': {
        'a': 1,
        'b': 1
    }
}

def create_dist(graph):
    dist = []
    for i in range(len(graph)):
        dist.append([float("inf")] * (len(graph)))
    print dist

def create_next(graph):
    dist = []
    for i in range(len(graph)):
        dist.append(["null"] * (len(graph)))
    print dist
    
create_dist(testgraph)
create_next(testgraph)

