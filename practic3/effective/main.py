import random
import time
from eff_func import closest_pair


N = int(input("N = "))
p = [{}]*N
for i in range(N):
    p[i] = {'x': round(random.uniform(-N, N)),
            'y': round(random.uniform(-N, N))}
t1 = time.perf_counter()
p = closest_pair(p)
t2 = time.perf_counter()
print(p, f"Время: {t2 - t1:0.4f}")
