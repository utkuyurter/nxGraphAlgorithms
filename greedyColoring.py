# -*- coding: utf-8 -*-
#Authors: Utku Yurter , Jonathan Menjivar
#Discrete Math - Graph Theory

from functions.globalProperties import V

def greedy_coloring(G):
    color_matching = {}
    for v in V(G):
        available = [True] * len(V(G))
        for n in G[v]:
            if n in color_matching:
                color = color_matching[n]
                available[color] = False
        for color, not_taken in enumerate(available):
            if not_taken:
                color_matching[v] = color
                break
    return color_matching
