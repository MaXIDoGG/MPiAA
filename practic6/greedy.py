import math


def TSP(G, start):
    if len(G) <= 1:
        return []
    current = start
    Path = [current]
    while len(Path) != len(G):
        minS = math.inf
        Next = math.inf
        for i in range(len(G)):
            if i not in Path:
                if G[current][i] < minS and G[current][i] != 0:
                    minS = G[current][i]
                    Next = i
        if Next == math.inf:
            return []
        Path.append(Next)
        current = Next
    if G[Path[-1]][start] == 0:
        return []
    return Path
