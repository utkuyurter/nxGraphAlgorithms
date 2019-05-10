# -*- coding: utf-8 -*-
#Authors: Utku Yurter , Jonathan Menjivar
#Discrete Math - Graph Theory

import networkx as nx
from itertools import combinations
from functions.globalProperties import V, N
from functions.localProperties import neighbors
from functions.booleanFunctions import is_independent


def maximum_independent_set(G):
    n = len(V(G))
    for k in range(N(G),1,-1):
        for S in combinations(V(G), k):
            if is_independent(G,list(S)) == True:
                return list(S)


def independence_number(G):
    return len(maximum_independent_set(G))
