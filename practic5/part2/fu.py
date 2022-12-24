import math


def Prim(G, s):
    if len(G) == 0 or len(G) == 1:
        return {}
    minWeight = {i: math.inf for i in range(len(G))}
    minWeight[s] = 0
    Q = [i for i in range(len(G))]
    parent = {}
    while len(Q) > 0:
        min = math.inf
        minIndex = 0
        for i in Q:
            if minWeight[i] < min:
                min = minWeight[i]
                minIndex = i
        u = Q.pop(Q.index(minIndex))
        for v in range(len(G)):
            if (G[v][u] != 0):
                if (v in Q and minWeight[v] > G[u][v]):
                    minWeight[v] = G[u][v]
                    parent[v] = u
    MST = set()
    for i in parent:
        tup = (G[parent[i]][i], parent[i], i)
        MST.add(tup)
    return MST
