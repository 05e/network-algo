# https://github.com/05e/network-algorithms

import sys

from network import Network
from algorithms.dijkstra import Dijkstra
from algorithms.kruskal import Kruskal
from algorithms.prim import Prim

if __name__ == '__main__':

    seed = 0
    if (len(sys.argv) > 1):
        seed = int(sys.argv[1])
    
    G = [
    #    A  B  C  D  E  F  G  H  
        [0, 0, 5, 2, 0, 0, 0, 0], # A
        [0, 0, 0, 4, 0, 8, 0, 0], # B
        [5, 0, 0, 0, 0, 0, 4, 0], # C
        [2, 4, 0, 0, 3, 0, 0, 7], # D
        [0, 0, 0, 3, 0, 0, 5, 2], # E 
        [0, 8, 0, 0, 0, 0, 0, 6], # F
        [0, 0, 4, 0, 5, 0, 0, 0], # G
        [0, 0, 0, 7, 2, 6, 0, 0]  # H
    ]
    N = Network(G, seed)

    G = [
    #    A  B  C  D  E  F  G  H  
        [0, 0, 0, 4, 3, 8, 9, 0],# A
        [0, 0, 0, 7, 0, 3, 0, 6],# B
        [0, 0, 0, 0, 0, 4, 5, 5],# C
        [4, 7, 0, 0, 6, 0, 0, 0],# D
        [3, 0, 0, 6, 0, 0, 0, 0],# E
        [8, 3, 4, 0, 0, 0, 0, 0],# F
        [9, 0, 5, 0, 0, 0, 0, 0],# G
        [0, 6, 5, 0, 0, 0, 0, 0] # H
    ]
    NN = Network(G, seed)

    G = [
    #    A  B  C  D  E  F  G  H  I  J  K  L
        [0, 3, 2, 0, 0, 3, 0, 7, 0, 0, 0, 0],# A
        [3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],# B
        [2, 0, 0, 2, 0, 3, 0, 0, 0, 0, 5, 0],# C
        [0, 0, 2, 0, 3, 0, 0, 0, 0, 0, 8, 0],# D
        [0, 1, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0],# E
        [3, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0],# F
        [0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 0, 0],# G
        [7, 0, 0, 0, 0, 0, 3, 0, 4, 0, 6, 3],# H
        [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 5],# I
        [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 4],# J
        [0, 0, 5, 8, 0, 0, 0, 6, 0, 0, 0, 0],# K
        [0, 0, 0, 0, 0, 0, 0, 3, 5, 4, 0, 0] # L
    ]
    NNN = Network(G, seed)

    N.drawNetwork()
    Dijkstra(N, 0)

    NN.drawNetwork()
    Prim(NN)

    NNN.drawNetwork()
    Kruskal(NNN)

    # if you want to create your own network, check out
    # https://graphonline.ru/en/ and import the adjacency list
    #  from graph -> adjacency list