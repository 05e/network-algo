# https://github.com/05e/network-algorithms

import sys

# n = node
# e = edge
# se = smallest edge
# sn = solution nodes
# mst = minimum spanning tree
class Prim():

    def __init__(self, N):
        self.N = N
        self.O = 0
        self.solve()

    def output(self, mst):
        mc = 0
        print('-- PRIM\'S ALGORITHM --')
        print('MST edges:')
        for e in mst:
            mc += e[2]
            print(chr(e[0] + ord('A')), '  -->  ', chr(e[1] + ord('A')), '(', e[2], ')')
            e.pop()
        print('Minimum Cost Spanning Tree: ', mc)
        print('Operations: ', self.O, '\n')
        self.N.drawSolution(mst)
        self.O = 0

    # basically selection sort
    def smallestEdge(self, n, sn):
        min = sys.maxsize
        min_index = 0
        for m in range(self.N.V):
            self.O = self.O + 1

            if self.N.G[n][m] > 0 and self.N.G[n][m] < min and m not in sn:
                min = self.N.G[n][m]
                min_index = m
        return [n, min_index, min]

    # O(V^2)
    def solve(self):
        mst = []
        sn = [0]

        # for V - 1:
        #   for all nodes in solution: 
        #       get nearest node
        #   add smallest nearest node to solution
        # (or)
        # Repeat for the number of Nodes - 1:
        # for every node in the solution, 
        # find the nearest node to x node
        # and compare it to the current nearest node
        # from the inital node ( Selection Sort )
        # When nearest node is found, add the edge
        # to that node to MST and the node itself to 
        # nodes in the solution
        for _ in range(self.N.V - 1):

            se = [0, 0, sys.maxsize]
            for n in sn:
                self.O = self.O + 1

                e = self.smallestEdge(n, sn)
                if e[2] < se[2]:
                    se = e
            sn.append(se[1])
            mst.append(se)

        self.output(mst)