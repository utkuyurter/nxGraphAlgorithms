# -*- coding: utf-8 -*-
#Authors: Utku Yurter , Jonathan Menjivar
#Discrete Math - Graph Theory

import networkx as nx
from greedyColoring import greedy_coloring
from independence import independence_number
from havelHakimi import residue
from matching import matching_number
from clique import clique_number
from prims import prims
from functions.weightedFunctionProperties import *

G = nx.read_edgelist("graph_library/G1.txt")
WG = nx.read_weighted_edgelist("graph_library/WG2.txt")

print(greedy_coloring(WG))
print(independence_number(WG))
print(residue(WG))
print(matching_number(WG))
print(clique_number(WG))
print(prims(WG, '2'))
