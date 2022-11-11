import time
import random
from func import get_max_activities

N = int(input('N = '))
S = []

for i in range(N):
    S.append([int(random.randint(0, N)), int(random.randint(0, N))])
    while (S[i][0] >= S[i][1]):
        N += 1
        S[i][1] = int(random.randint(0, N))

# S = sorted(S, key=lambda x: x[1])

t1 = time.perf_counter()
ans = get_max_activities(S)
t2 = time.perf_counter()

print(f"Время: {t2 - t1:0.4f}")
