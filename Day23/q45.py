"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q45.py (c) 2024
Desc: description
Created:  2024-12-22T21:15:36.780Z
Modified: 2024-12-23T08:15:30.032Z
"""

from time import time

graph = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        one, two = line.strip().split("-")

        if one not in graph:
            graph[one] = []
        if two not in graph:
            graph[two] = []

        graph[one].append(two)
        graph[two].append(one)


def find_cycles_length_3(graph):
    visited = set()
    cycles = set()

    def dfs(node, start, depth, path):
        if depth == 3:  # Base case: Check for a cycle of length 3
            if start in graph[node]:  # If we can go back to the start node
                cycle = tuple(sorted(path)) 
                cycles.add(cycle)
            return

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in path:  # Avoid revisiting nodes in the current path
                dfs(neighbor, start, depth + 1, path + [neighbor])
        visited.remove(node)

    for node in graph:
        if node.startswith("t"):
            # Only need to consider nodes that start with t, otherwise no need to explore
            dfs(node, node, 1, [node])  # Start DFS from each node

    return [list(cycle) for cycle in cycles]


t0 = time()
threecycles = find_cycles_length_3(graph)

print("Cycles with a node that starts with T:", threecycles)
print("Number of cycles with T:", len(threecycles))
print("Time taken:", time() - t0)
