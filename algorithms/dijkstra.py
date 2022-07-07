# https://github.com/05e/network-algorithms

import sys


# pn = picked node
# an = adjacent node
# n = node
# dl = distance label
# pl = permanent label
# spt = shortest path tree
# p = parent
# pi = parent index
# ci = child index
# sp = shortest path
class Dijkstra():

    def __init__(self, N, sn, fn=-1):
        self.N = N
        self.solve(sn, fn)

    def output(self, dl, sn, spt, fn):
        print('Node      SP from', chr(sn + ord('A')))
        for n in range(self.N.V):
            path = '-'.join([chr(spt[n][m] + ord('A')) for m in range(len(spt[n]))])
            print(chr(n + ord('A')), '  -->  ', path, '(', dl[n], ')')
        self.N.drawSolution(spt, fn)

        
# Example SPT Solution
#
#          A
#        /  \  \
#       F    B  E
#      / \       \
#     C   D       D

# SPT = [ [], [0,1], [0,5,2], [0,5,3], [0,4], [0,5] ]
# Notice that each SP starts with sn and ends with n


    def nearestNode(self, dl, pl):
        min = sys.maxsize
        min_index = 0

        # basically selection sort
        for n in range(self.N.V):
            if dl[n] < min and pl[n] == False:
                min = dl[n]
                min_index = n

        return min_index

    # O(V^2) 
    # Can be reduced to O(ElogV) with binary heap if looking for specific fn
    def solve(self, sn, fn):
        dl = [sys.maxsize] * self.N.V
        dl[sn] = 0
        pl = [False] * self.N.V
        
        p = [None] * self.N.V
        p[sn] = -1

        for n in range(self.N.V):
            # Find nearest node from n not yet processed
            pn = self.nearestNode(dl, pl)
            pl[pn] = True


            # If distance label of adjacent node is LARGER THAN
            # the distance label of picked node + distance pn->an,
            # Update distance label of adjacent node 
            # BUT if adjacent node already has P. Label, ignore
            # (or)
            # If dl[an] > dl[pn] + (pn->an)
            # Then dl[an] = dl[pn]+(pn->an) IF !pl[an]
            for an in range(self.N.V):

                if self.N.G[pn][an] > 0 and pl[an] == False and dl[an] > dl[pn] + self.N.G[pn][an]:
                    dl[an] = dl[pn] + self.N.G[pn][an]
                    p[an] = pn  # Set parent of an = pn

        # Construct spt based on list of parents.
        # For each node, if parent != sn,
        # prepend parent of parent to sp of node,
        # repeat until parent = sn
        spt = [[]] * self.N.V
        spt[sn] = [sn]
        for n in range(self.N.V):
            if n != sn:
                ci = n 
                pi = p[n] 
                sp = [pi, ci]
                while pi != sn:
                    pi = p[pi] 
                    sp.insert(0, pi)
                spt[ci] = sp

        self.output(dl, sn, spt, fn)