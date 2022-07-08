# https://github.com/05e/network-algorithms


from network import Network
# surely there's a better way to do this?
from algorithms.dijkstra import Dijkstra
from algorithms.kruskal import Kruskal
from algorithms.prim import Prim

if __name__ == '__main__':
    N = Network(8, 1337)
    N.G = [
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

    NN = Network(8, 1337)
    NN.G = [
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

    NNN = Network(12, 1337)
    NNN.G = [
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

    N.drawNetwork()
    Dijkstra(N, 0)

    NN.drawNetwork()
    Prim(NN)

    NNN.drawNetwork()
    Kruskal(NNN)

    # if you want to create your own network, check out
    # https://graphonline.ru/en/ and import the adjacency list
    # from graph -> adjacency list