# -*- coding: utf-8 -*-
#Authors: Utku Yurter , Jonathan Menjivar
#Discrete Math - Graph Theory

from functions.globalProperties import E
from functions.localProperties import neighbors

def edge_cost(G, e):
    c = G.get_edge_data(e[0], e[1])
    return c['weight']


def minimum_incident_edge(G, T):
    incidentEdge = incident_edges(G, T)
    minIncident = incidentEdge[0]
    for edge in incidentEdge:
        if edge_cost(G, edge) < edge_cost(G, minIncident):
            minIncident = edge
    return minIncident


def incident_edges(G, T):
    incident_e = []
    for e in E(G):
        if ((e[0] in T[0]) or (e[1] in T[0])) and (e not in T[1]):
                incident_e.append(e)
    return incident_e
