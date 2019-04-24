# -*- coding: utf-8 -*-
#Author: Utku Yurter , University Of Houston - Downtown
#Discrete Math - Graph Theory

import networkx as nx


def neighbors(G, v):
    return list(nx.neighbors(G,v))
