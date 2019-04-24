# -*- coding: utf-8 -*-
#Author: Utku Yurter , University Of Houston - Downtown
#Discrete Math - Graph Theory

import networkx as nx
from itertools import combinations
from functions.globalProperties import V, N
from functions.localProperties import neighbors


def is_independent (G, S):
    for v in S:
        if list(set(S) & set(neighbors(G, v))) !=[]:
            return False
    return True


def maximum_independent_set(G):
    n = len(V(G))
    for k in range(N(G),1,-1):
        for S in combinations(V(G), k):
            if is_independent(G,list(S)) == True:
                return list(S)


def independence_number(G):
    return len(maximum_independent_set(G))
