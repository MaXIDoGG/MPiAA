from fu import Cruskal, Prim
import random as ran
import time

N = int(input('N(Кол-во вершин) = '))
G = []
for i in range(N):
    G.append([0]*N)

for i in range(N):
    for j in range(i+1, N):
        if j >= N:
            break
        G[i][j] = int(ran.randint(1, N))
        G[j][i] = G[i][j]

t1 = time.perf_counter()
MST = Prim(G, 0)
t2 = time.perf_counter()

print(f"Время: {t2 - t1:0.4f}")
