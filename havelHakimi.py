# -*- coding: utf-8 -*-
#Authors: Utku Yurter , Jonathan Menjivar
#Discrete Math - Graph Theory

from functions.globalProperties import degree_sequence, V
from functions.localProperties import neighbors


def Havel_Hakimi_derivative(L):
    assert len(L) != 0, 'List Cannot Be Empty'
    d_1 = L[0]
    L.pop(0)
    for i in range(d_1):
        L[i] -= 1
    L.sort(reverse=True)
    return None

def H_H_process(L, show=False):
    if show:
        print(L)
    while L[0] > 0:
        Havel_Hakimi_derivative(L)
        if show:
            print(L)
    return None

def residue(G):
    L = degree_sequence(G)
    H_H_process(L)
    return(len(L))
