from func import nativeLcs
import time

x = input('x = ')
y = input('y = ')

t1 = time.perf_counter()
LCS = nativeLcs(x, y)
t2 = time.perf_counter()

print(LCS, f"Время: {t2 - t1:0.4f}")
