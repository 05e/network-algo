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

    #N.drawNetwork()
    #N.printNetwork()
    
    Dijkstra(N, 0, 5)
    #Kruskal(N)
    #Prim(N)