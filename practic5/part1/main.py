import random as ran
import time
from fu import Dijkstra

N = int(input('N(Кол-во вершин) = '))
G = []
for i in range(N):
    G.append([0]*N)

for i in range(N):
    flag1 = False
    while(flag1 == False):
        for j in range(i+1, N):
            if j >= N:
                break
            flag2 = int(ran.randint(0, 1))
            if flag2 == 1:
                G[i][j] = int(ran.randint(1, N))
                G[j][i] = G[i][j]
        if G[i] != [0]*N:
            flag1 = True

t1 = time.perf_counter()
path = Dijkstra(G, 0, N-1)
t2 = time.perf_counter()

print(path, f"Время: {t2 - t1:0.4f}")