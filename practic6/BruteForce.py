import math


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


# def TSP(G, start):
#     if len(G) <= 1:
#         return []
#     cities = [i for i in range(len(G))]
#     minS = math.inf
#     minPerm = []
#     perms = permutation(cities)
#     for perm in perms:
#         s = 0
#         if perm[0] == start:
#             for i in range(len(perm)):
#                 if i == len(perm) - 1:
#                     break
#                 if G[perm[i]][perm[i+1]] == 0:
#                     s = math.inf
#                     break
#                 s += G[perm[i]][perm[i+1]]
#             if s < minS:
#                 minS = s
#                 minPerm = perm
#     return minPerm


def TSP(G, start):
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
