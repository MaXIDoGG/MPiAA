from Func import TSP_Pereb, TSP_Greedy, TSP_BnB, Length 
import math
import random as ran
import time

N = int(input('N(Кол-во вершин) = '))
G = []
for i in range(N):
    G.append([math.inf]*N)

for i in range(N):
    for j in range(i+1, N):
        if j >= N:
            break
        G[i][j] = int(ran.randint(1, N))
        G[j][i] = G[i][j]
    

# t1 = time.perf_counter()
# L1 = TSP_BnB(G, 0)
# t2 = time.perf_counter()

# print(Length(L1,G), f"Время: {t2 - t1:0.4f}")

t1 = time.perf_counter()
L2 = TSP_Pereb(G, 0)
t2 = time.perf_counter()

print(Length(L2,G), f"Время: {t2 - t1:0.4f}")

# t1 = time.perf_counter()
# L3 = TSP_Greedy(G, 0)
# t2 = time.perf_counter()

# print(Length(L3,G), f"Время: {t2 - t1:0.4f}")
