# -*- coding: utf-8 -*-
#Authors: Utku Yurter , Jonathan Menjivar
#Discrete Math - Graph Theory


from functions.globalProperties import V
from functions.weightedFunctionProperties import minimum_incident_edge, edge_cost

def prims(G, v):
    T = ([v], [])
    while set(T[0]) != set(V(G)):
        e = minimum_incident_edge(G, T)
        T[1].append(e)
        if (e[0] not in T[0]) and (e[1] in T[0]):
            T[0].append(e[0])
        elif (e[0] in T[0]) and (e[1] not in T[0]):
            T[0].append(e[1])
        elif (e[0] not in T[0]) and (e[1] not in T[0]):
            T[0].append(e[0])
            T[0].append(e[1])
        else:
            continue
    return T, sum([edge_cost(G, e) for e in T[1]])
