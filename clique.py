# -*- coding: utf-8 -*-
#Author: Utku Yurter , University Of Houston - Downtown
#Discrete Math - Graph Theory


from functions.globalProperties import E, V, N
from itertools import combinations


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


#def max_clique(G):




#def clique_number(G):
#    return len(max_clique(G))


def is_triangle_free(G, S):
    if is_Clique(G, S) and len(S) == 3:
        return False
    else:
        return True
