"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q45.py (c) 2024
Desc: description
Created:  2024-12-22T21:15:36.780Z
Modified: 2024-12-23T08:10:33.034Z
"""

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


ans = []
def bron_kerbosch(P, R, X, graph):
    '''
    R: The current clique being constructed. (list)
    P: The potential nodes that could be added to the current clique. (set)
    X: The nodes that have been excluded from the current clique (these are explored in previous iterations). (set)
    '''
    if not P and not X:
        ans.append(set(R))
        return

    for v in set(P): #Use set(P) to make a copy and iterate over that since we do P.remove(v)
        neighbors = set(graph[v])
        bron_kerbosch(P & neighbors, R + [v], X & neighbors, graph)
        P.remove(v)
        X.add(v)


bron_kerbosch(set(graph.keys()), [], set(), graph)
print(ans)

print("Maxmial clique:", ",".join(sorted(list(max(ans, key=len)))))
