# -*- coding: utf-8 -*-
#Author: Utku Yurter , University Of Houston - Downtown
#Discrete Math - Graph Theory

import networkx as nx
from greedyColoring import greedy_coloring
from independence import independence_number
from havelHakimi import residue
from matching import matching_number
from clique import clique_number

G = nx.read_edgelist("graph_library/G1.txt")

# M1 = [('0', '1'), ('4', '6')]
# M2 = [('0', '1'), ('2', '3'), ('0', '2')]
# IS1 = ['0', '6', '10']
# IS2 = ['0', '8', '9']
# C1 = [('0' , '1'), ('1', '2'), ('0', '2')]
# C2 = [('0' , '3'), ('0', '2'), ('0', '1')]
# C3 = [('0', '1')]
#
# D = {
#     '0' : 'A',
#     '1' : 'B',
#     '2' : 'C',
#     '3' : 'A',
#     '4' : 'B' ,
#     '5' : 'C',
#     '6' : 'A',
#     '7' : 'B' ,
#     '8' : 'C',
#     '9' : 'A'
#     }

print(greedy_coloring(G))
print(independence_number(G))
print(residue(G))
print(matching_number(G))
print(clique_number(G))
