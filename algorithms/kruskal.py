# https://github.com/05e/network-algorithms

# e = edges
# n = node
# p = parent
# r = rank
# ne = next edge
# mst = minimum spanning tree
# si = solution index
# mc = minimum cost

class Kruskal():
    def __init__(self, N):
        self.N = N
        self.solve()

    def output(self, mst):
        mc = 0
        print('MST edges:')
        for e in mst:
            mc += e[2]
            print(chr(e[0] + ord('A')), '  -->  ', chr(e[1] + ord('A')), '(', e[2], ')')
            e.pop()
        print('Minimum Cost Spanning Tree: ', mc)
        self.N.drawSolution(mst)


    # Bubble sort
    # O(n^2)
    def sort(self, e, k):
        for i in range(len(e)):
            for j in range(len(e) - 1):
                if e[j][k] > e[j+1][k]:
                    e[j], e[j+1] = e[j+1], e[j]
                

    # Find-Union by Rank algorithm used
    # for proper loop detection in network
    def find(self, p, i):
        if p[i] == i:
            return i
        return self.find(p, p[i])

    def union(self, p, r, n, m):
        np = self.find(p, n)
        mp = self.find(p, m)

        if r[np] < r[mp]:
            p[np] = mp
        elif r[mp] < r[np]:
            p[mp] = np
        else:
            p[mp] = np
            r[np] = r[np]+1
        

    def solve(self):
        # Get list of all edges (directional included) 
        e = []
        for n in range(self.N.V):
            for m in range(self.N.V):
                if self.N.G[n][m] > 0:
                    e.append([n, m, self.N.G[n][m]]) 
        
        # Sort e in ascending order for Kruskal
        self.sort(e, 2)

        p = []
        r = []
        for n in range(self.N.V):
            p.append(n)
            r.append(0)

        mst = []
        i = 0
        si = 0
        while si < self.N.V - 1:
            # Pick next edge in array and increase i for next iteration
            ne = e[i]
            i = i+1
            n = self.find(p, ne[0])
            m = self.find(p, ne[1])

            # If origin node isn't destination node,
            # aka adding the origin node to MST wouldn't create a loop,
            # add ne to MST and increase solution index
            if n != m:
                si = si+1
                mst.append(ne)
                self.union(p, r, n, m)
        
        self.output(mst)




    # this is my first attempt at a 
    # kruskal implementation which
    # (surprisingly!) doesn't function 
    # correctly. The reason for that is 
    # that the loop detecting method isn't
    # accurate as it only checks the 
    # destination node for a loop, instead of 
    # recursively identifying parent nodes.
    #
    # I left this here because so people
    # may learn from my mistakes 
    def solve_broken(self):
    
        # Get list of all edges (directional included) 
        e = []
        for n in range(self.N.V):
            for m in range(self.N.V):
                if self.N.G[n][m] > 0:
                    e.append([n, m, self.N.G[n][m]]) 
        
        # Sort e in ascending order for Kruskal
        self.sort(e, 2)
        
        # Set up mst, sn, i, si for algorithm
        # While the list of solution nodes is smaller
        # than the total number of nodes - 1 ( |V| - 1 ):
        # Get next edge in sorted edge list,
        # if the destination node of this edge is not in
        # the solution AND the opposite direction of this edge 
        # is not in mst, add edge to mst and add destination node to sn
        # (or)
        # while sn < V-1:
        #   if ne[dn] not in sn and other direction of ne not in mst:
        #       mst += ne
        #       sn += ne[dn]
        mst = []
        sn = []

        i = 0
        si = 0
        while len(sn) < self.N.V:
            ne = e[i]
            i = i+1
            if ne[1] not in sn and [ne[1], ne[0], ne[2]] not in mst:
                mst.append(ne)
                sn.append(ne[1])
                si = si+1

        self.output(mst)