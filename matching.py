# -*- coding: utf-8 -*-
#Authors: Utku Yurter , Jonathan Menjivar
#Discrete Math - Graph Theory


from functions.globalProperties import N, E
from functions.booleanFunctions import is_matching

def max_matching(G):
    Vertex = set()
    max_matching = set()
    for u, v in E(G):
        if u not in Vertex and v not in Vertex and u != v:
            max_matching.add((u, v))
            Vertex.add(u)
            Vertex.add(v)
    return max_matching

def matching_number(G):
    return len(max_matching(G))
