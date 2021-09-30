"""
Dijkstra's Algorithm
Author: Erin
Date: 5/14/21

With help from: Michael Tulskikh
"""
import random
from datetime import datetime


# Find next vertex to visit
def findNext(paths,un):
    temp = float("inf")
    key = -1
    for u in un:
        if paths[str(u)] < temp:
            temp = paths[str(u)]
            key = u
    return key

# Runs dijkstra's algorithm
def dijkstra(W, startVertexValue):
    # start the clock!
    start=datetime.now()

    # Get num vertices
    n = len(W)

    # Get unvisited vertices
    unvisited = []
    for i in range(n):
        unvisited.append(i)

    # Initialize start vertex and visit it
    startVertex = startVertexValue
    unvisited.remove(startVertex)

    # Initialize dictionary
    shortestPaths = {}
    for i in range(n):
        shortestPaths[str(i)] = float('inf')
    shortestPaths[str(startVertex)] = 0
    for idx, value in enumerate(W[startVertex]):
        if idx != startVertex and value != float('inf'):
            shortestPaths[str(idx)] = value

    # Finding direct paths from starting vertex
    tempMin = float('inf')
    for u in unvisited:
        if shortestPaths[str(u)] < tempMin:
            tempMin = shortestPaths[str(u)]
            nextVertex = u

    # Find the rest of unvisited vertex paths using visited as intermediates
    while unvisited:
        for u in unvisited:
            # Check if going thru intermediate vertex is less expensive than direct route
            if shortestPaths[str(nextVertex)] + W[nextVertex][u] < shortestPaths[str(u)]:
                shortestPaths[str(u)] = shortestPaths[str(nextVertex)] + W[nextVertex][u]
        unvisited.remove(nextVertex)
        if not unvisited:
            break
        nextVertex = findNext(shortestPaths, unvisited)
    print("\nShortest paths to each vertex:")
    print(shortestPaths)
    print(f"\nRuntime for graph of {n} vertices:" + str(datetime.now()-start) + "\n")

# Run dijkstra's algorithm with graphs of different sizes
for i in range(5, 100, 20):
    dijkstra([[random.randint(0, 20) for x in range(i)] for y in range(i)], 0)
    

