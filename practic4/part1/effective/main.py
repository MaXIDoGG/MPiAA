from func import LCS_DYN
import time

x = input('x = ')
y = input('y = ')

t1 = time.perf_counter()
LCS = LCS_DYN(x, y)
t2 = time.perf_counter()

print(str(LCS), f"Время: {t2 - t1:0.4f}")
