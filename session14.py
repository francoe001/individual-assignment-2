#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 11:37:32 2018

@author: efrancois
"""

#white belt
#Create a function non_connected to find non-connected nodes in a graph

g = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["d"],
        "d": [],
        "e":[]
}

def non_connected(g):
    
    non_connected_nodes = []
    
    outgoing_edges = []
    
    for node in g:
        for outgoing_edge in g[node]:
            outgoing_edges.append(outgoing_edge)
            
    for node in g:
        if g[node] == [] and node not in outgoing_edges:
            non_connected_nodes.append(node)
    
    return non_connected_nodes





#%%
    
#blue belt
#Create a function fully_connected to that returns True if a graph is fully connected, 
#False otherwise

g = {
     "a": ["b","c"],
     "b": ["c", "a"],
     "c": ["a", "b"]
     }

def fully_connected(g):
    nodes = len(list(g.keys()))
    edges = []
    
    for node in g:
        for edge in g[node]:
            edges.append(edge)
    return len(edges) == nodes * (nodes - 1)
        
        
# A fully connected graph with n nodes has  n * n - 1 edges



#%%
    
#black belt
#Implement weighted graphs

#Create a cheapest_path function that returns the cheapest path between two points in a weighted 
#graph