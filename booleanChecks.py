# -*- coding: utf-8 -*-
#Author: Utku Yurter , University Of Houston - Downtown
#Discrete Math - Graph Theory


from functionsClass import *
from itertools import combinations


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


def is_independent_set(G, S):
    result = True
    for e in S:
        for v in S:
            if (e , v) in E(G):
                result = False
                break
    return result


def is_Clique(G, S):
    result = True
    lst = []
    for e in S:
        lst.append(e[0])
        lst.append(e[1])
    for e in lst:
        if len(S) == 1 and S[0] in E(G):
            result = True
            break
        if lst.count(e) != len(S) - 1:
                result = False
                break
    return result



def is_triangle_free(G, S):
    if is_Clique(G, S) and len(S) == 3:
        return False
    else:
        return True
