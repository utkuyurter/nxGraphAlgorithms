# -*- coding: utf-8 -*-
#Author: Utku Yurter , University Of Houston - Downtown
#Discrete Math - Graph Theory

import networkx as nx
from functions.localProperties import neighbors

def V(G):
    return nx.nodes(G)

def E(G):
    return nx.edges(G)

def N(G):
    return len(V(G))

def M(G):
    return len(E(G))

def degree(G, v):
    return len(neighbors(G,v))

def degree_sequence(G):
    D = [degree(G,v) for v in V(G)]
    D.sort(reverse=True)
    return D

def maximum_degree(G):
    return degree_sequence(G)[0]

def minimum_degree(G):
    return degree_sequence(G)[-1]

def average_degree(G):
    return sum(degree_sequence(G)) / N(G)

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

def eccentricity(G, v):
    return len(distance_array(G, v)) - 1

def radius(G):
    return min([eccentricity(G, v) for v in V(G)])

def diameter(G):
    return max([eccentricity(G, v) for v in V(G)])

#Find the center of the graph, which returns the center vertices in the graph
def graph_center(G):
    return [v for v in V(G) if eccentricity(G,v) == radius(G)]
