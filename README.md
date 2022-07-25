# network-algorithms
Python implementations of common network algorithms and network visualization through networkx

![Image of Matplotlib Visualization](https://i.imgur.com/VLfnEXs.png "Visualization")

## algorithms
- **Dijkstra**'s Shortest Path Algorithm
- **Kruskal**'s Minimum Spanning Tree Algorithm
- **Prim**'s Minimum Spanning Tree Algorithm

## network representation
Networks are represented with an adjacency matrix
e.g.
```py
[0, 0, 5, 2],
[0, 0, 0, 4],
[5, 0, 0, 0],
[2, 4, 0, 0]
```

## main functions
```py
# Algorithms:
Dijkstra(Network N, int Starting Node, [int Finish Node]) # Run and Display Dijkstra's Algorithm
Kruskal(Network N) # Run and Display Kruskal's Algorithm
Prim(Network N) # Run and Display Prim's Algorithm
# Network:
Network(int[] AdjacencyMatrix, [int Seed]) # Initialize network with given adjacency matrix
Network.drawNetwork() # Show network through plotmatlib
Network.printNetwork() # Print network in terminal
```
