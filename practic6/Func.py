import math
def MinPath(P1, P2, G):
    return min(P1, P2, key=lambda i: Length(i, G))

def Length(Path, G):
    s = 0
    for i in range(len(Path)):
        if i == len(Path) - 1:
            break
        s += G[Path[i]][Path[i+1]]
    return s

def LowerBound(G, Vis):
    if G[Vis[-1]][Vis[-2]] == 0:
        return []
    V = Vis[:]
    dot = V[-1]
    min = math.inf
    if len(V) == len(G):
        return Length(V, G)
    elif len(V) <= len(G):
        for i in range(len(G)):
            if i not in V and min > G[dot][i]:
                min = G[dot][i]
                h = i
        V.append(h)
        return LowerBound(G, V)
    
def BnB(G, visited, BestPath):
    if len(visited) == len(G):
        return MinPath(BestPath, visited, G)
    for v in range(len(G)):
        if v in visited:
            continue
        else:
            VNext = visited[:]
            VNext.append(v)
            LB = LowerBound(G, VNext)
            if LB == []:
                return []
            else:
                if LB < Length(BestPath, G):
                    Path = BnB(G, VNext, BestPath)
                    BestPath = MinPath(BestPath, Path, G)
    else:
        return BestPath

def TSP_BnB(G, start):
    if len(G) <= 1:
        return []
    visited = [start]
    BestPath = [start]
    for i in range(len(G)):
        min = math.inf
        for j in range(len(G)):
            if j not in BestPath and G[i][j] != 0:
                if min > G[i][j]:
                    min = G[i][j]
        if min == math.inf:
            continue
        else:
            BestPath.append(G[i].index(min))
    return BnB(G, visited, BestPath)

def permutation(s):
    if len(s) == 1:
        return [s]
    perm_list = []  # resulting list
    for a in s:
        remaining_elements = [x for x in s if x != a]
        z = permutation(remaining_elements)  # permutations of sublist
        for t in z:
            perm_list.append([a] + t)
    return perm_list

def TSP_Pereb(G, start):
    if len(G) <= 1:
        return []
    cities = [i for i in range(len(G))]
    minS = math.inf
    minPerm = []
    perms = permutation(cities)
    for perm in perms:
        s = 0
        if perm[0] == start:
            for i in range(len(perm)):
                if i == len(perm) - 1:
                    break
                if G[perm[i]][perm[i+1]] == 0 or G[perm[len(perm)-1]][start] == 0:
                    s = math.inf
                    break
                else:
                    s += G[perm[i]][perm[i+1]]
            if s < minS:
                minS = s
                minPerm = perm
    return minPerm

def TSP_Greedy(G, start):
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