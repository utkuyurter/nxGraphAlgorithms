# -*- coding: utf-8 -*-
#Authors: Utku Yurter , Jonathan Menjivar
#Discrete Math - Graph Theory

import networkx as nx


def neighbors(G, v):
    return list(nx.neighbors(G,v))

def degree(G, v):
    return len(neighbors(G,v))


#Create an array of all vertices in relation to their distance to vertex v
def distance_array(G, v):
    N = [[v]]
    Obs = [v]
    while set(Obs) != set(V(G)):
        temp_neighbors = []
        for x in N[-1]:
            for y in neighbors(G, x):
                if y not in Obs:
                    temp_neighbors.append(y)
                    Obs.append(y)
        N.append(temp_neighbors)
    return N

#Return distance from vertex v to vertex w
def distance(G, v , w):
    D = distance_array(G, v)
    for i in range(len(D)):
        if w in D[i]:
            return i
