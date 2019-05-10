# -*- coding: utf-8 -*-
#Authors: Utku Yurter , Jonathan Menjivar
#Discrete Math - Graph Theory


from functions.localProperties import neighbors
from havelHakimi import H_H_process

def is_Clique(G, S):
    for v in S:
        N = neighbors(G, v)
        if list(set(N) & set(S)) !=[]:
            return False
    return True

def is_triangle_free(G, S):
    if is_Clique(G, S) and len(S) == 3:
        return False
    else:
        return True

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


def is_independent (G, S):
    for v in S:
        if list(set(S) & set(neighbors(G, v))) !=[]:
            return False
    return True

def isGraphic(L):
    H_H_process(L)
    return sum(L) == 0
