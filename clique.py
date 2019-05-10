# -*- coding: utf-8 -*-
#Authors: Utku Yurter , Jonathan Menjivar
#Discrete Math - Graph Theory

from functions.globalProperties import V, N
from itertools import combinations
from functions.booleanFunctions import is_Clique


def max_clique(G):
    for c in range (N(G), 1, -1):
        for v in combinations(V(G), c):
            if is_Clique(G, list(v)) == True:
                return list(v)

def clique_number(G):
    return len(max_clique(G))
