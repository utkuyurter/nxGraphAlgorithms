# -*- coding: utf-8 -*-
#Authors: Utku Yurter , Jonathan Menjivar
#Discrete Math - Graph Theory

import networkx as nx
from functions.localProperties import neighbors, degree, distance_array

def V(G):
    return nx.nodes(G)

def E(G):
    return nx.edges(G)

def N(G):
    return len(V(G))

def M(G):
    return len(E(G))

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

def eccentricity(G, v):
    return len(distance_array(G, v)) - 1

def radius(G):
    return min([eccentricity(G, v) for v in V(G)])

def diameter(G):
    return max([eccentricity(G, v) for v in V(G)])

#Find the center of the graph, which returns the center vertices in the graph
def graph_center(G):
    return [v for v in V(G) if eccentricity(G,v) == radius(G)]
