# https://github.com/05e/network-algorithms

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class Network():
    def __init__(self, vertices, seed=8):
        self.V = vertices
        self.G = [[0] * vertices] * vertices
        self.seed = seed

    def printNetwork(self):
        print('  '.join([chr(n + ord('A')) for n in range(self.V)]))
        for row in range(self.V):
            for column in self.G[row]:
                print(column, end='  ')
            print(chr(row + ord('A')))
        print()

    def drawNetwork(self):
        npG = np.asmatrix(self.G)
        nxG = nx.from_numpy_array(npG)

        pos = nx.spring_layout(nxG, seed=self.seed)

        # nodes & edges
        nx.draw_networkx_nodes(nxG, pos, node_size=700)
        nx.draw_networkx_edges(nxG, pos, width=2)

        # node & edges labels
        title_list = [chr(n + ord('A')) for n in range(self.V)]
        node_labels = dict(zip(nxG.nodes, title_list))
        nx.draw_networkx_labels(nxG, pos, font_size=20, labels=node_labels, font_family="sans-serif")

        edge_labels = nx.get_edge_attributes(nxG, "weight")
        nx.draw_networkx_edge_labels(nxG, pos, edge_labels)

        plt.axis('off')
        plt.show()
        
    def drawSolution(self, sol, fn=-1):
        npG = np.asmatrix(self.G)
        nxG = nx.from_numpy_array(npG)

        pos = nx.spring_layout(nxG, seed=self.seed)

        # nodes & edges
        if fn >= 0:
            nsol = [(n) for n in sol[fn]]
            nout = nxG.nodes - nsol
            nx.draw_networkx_nodes(nxG, pos, nodelist=nsol, node_size=800, node_color="tab:red")
            nx.draw_networkx_nodes(nxG, pos, nodelist=nout, node_size=700, node_color="tab:gray")
        else: 
            nsol = [(n) for m in range(len(sol)) for n in sol[m]] # all nodes will always be part of the solution as fn < 0
            nout = nxG.nodes - nsol
            nx.draw_networkx_nodes(nxG, pos, nodelist=nsol, node_size=800, node_color="tab:red")
            nx.draw_networkx_nodes(nxG, pos, nodelist=nout, node_size=700, node_color="tab:gray")

        if fn >= 0:
            esol = [tuple(sorted((sol[fn][n], sol[fn][n+1]))) for n in range(len(sol[fn])-1)] # tuples have to be sorted for subtraction in networkx
            eout = nxG.edges - esol
            nx.draw_networkx_edges(nxG, pos, edgelist=esol, width=3, edge_color="tab:red")
            nx.draw_networkx_edges(nxG, pos, edgelist=eout, width=2, style="dashed", edge_color="tab:gray")
        else:
            esol = [tuple(sorted((sol[m][n], sol[m][n+1]))) for m in range(len(sol)) for n in range(len(sol[m])-1) ] # tuples have to be sorted for subtraction in networkx
            eout = nxG.edges - esol
            nx.draw_networkx_edges(nxG, pos, edgelist=esol, width=3, edge_color="tab:red")
            nx.draw_networkx_edges(nxG, pos, edgelist=eout, width=2, style="dashed", edge_color="tab:gray")
            #nx.draw_networkx_edges(nxG, pos, width=3)

        # node & edges labels
        title_list = [chr(n + ord('A')) for n in range(self.V)]
        node_labels = dict(zip(nxG.nodes, title_list))
        nx.draw_networkx_labels(nxG, pos, font_size=20, labels=node_labels, font_family="sans-serif")

        edge_labels = nx.get_edge_attributes(nxG, "weight")
        nx.draw_networkx_edge_labels(nxG, pos, edge_labels)

        plt.axis('off')
        plt.show()