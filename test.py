# -*- coding: utf-8 -*-
#Author: Utku Yurter , University Of Houston - Downtown
#Discrete Math - Graph Theory

import networkx as nx
from functionsClass import *
from booleanChecks import *

#print(average_degree(G))
#H = nx.davis_southern_women_graph()
#nx.draw(H)
#print(f'minimum_degree: {minimum_degree(H)}')
#print('')
#print(f'maximum_degree: {maximum_degree(H)}')
#print('')
#print(f'average_degree: {average_degree(H)}')
#print('')
#print(f'V(H):= {V(H)}')
#print('')
#print(f'E(H):= {E(H)}')

G = nx.read_edgelist("T.txt")
#nx.draw(G)
#L = [3, 3, 3, 2, 2, 1]
#D = []
#H_H_process(L, show=True)
#print(Havel_Hakimi_derivative(L))
#print(L)
#print(isGraphic(L))
#print(residue(G))

M1 = [('0', '1'), ('4', '6')]
M2 = [('0', '1'), ('2', '3'), ('0', '2')]
IS1 = ['0', '6', '10']
IS2 = ['0', '8', '9']
C1 = [('0' , '1'), ('1', '2'), ('0', '2')]
C2 = [('0' , '3'), ('0', '2'), ('0', '1')]
C3 = [('0', '1')]

D = {
    '0' : 'A',
    '1' : 'B',
    '2' : 'C',
    '3' : 'A',
    '4' : 'B' ,
    '5' : 'C',
    '6' : 'A',
    '7' : 'B' ,
    '8' : 'C',
    '9' : 'A'
    }

#print(is_matching(G, M1))
#print(is_matching(G, M2))
#print(is_independent_set(G, IS1))
#print(is_independent_set(G, IS2))
#print(is_Clique(G, C1))
#print(is_Clique(G, C2))
#print(is_Clique(G, C3))
#print(is_triangle_free(G, C1))
#print(is_triangle_free(G, C2))
#print(is_triangle_free(G, C3))
#print(D.keys())
#print(V(G))
#print(is_colored('2', D))
#print(all_colored(G, D))
#print(same_color('0', '3', D))
print(proper_coloring(G))
