# -*- coding: utf-8 -*-
#Author: Utku Yurter , University Of Houston - Downtown
#Discrete Math - Graph Theory


from functions.globalProperties import N, E


def is_matching(G, M):
    result = True
    lst = []
    for e in M:
        lst.append(e[0])
        lst.append(e[1])
    for e in lst:
        if(lst.count(e) > 1):
            result = False
    return result

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
