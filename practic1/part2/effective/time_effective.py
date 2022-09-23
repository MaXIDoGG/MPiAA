import time
import random
from effective_duplicates import has_duplicates, get_duplicates

N = int(input())


arrEqual = [10 for i in range(N)]

arrRandom = [round(random.random()*10) for i in range(N)]

arrVarious = [i for i in range(N)]


print('IDENTICAL VALUES\n')
t1 = time.perf_counter()
print(has_duplicates(arrEqual))
t2 = time.perf_counter()
print(f"Вычисление заняло {t2 - t1:0.4f} секунд")

t1 = time.perf_counter()
print(get_duplicates(arrEqual))
t2 = time.perf_counter()
print(f"Вычисление заняло {t2 - t1:0.4f} секунд\n")


print('RANDOM VALUES\n')
t1 = time.perf_counter()
print(has_duplicates(arrRandom))
t2 = time.perf_counter()
print(f"Вычисление заняло {t2 - t1:0.4f} секунд")

t1 = time.perf_counter()
print(get_duplicates(arrRandom))
t2 = time.perf_counter()
print(f"Вычисление заняло {t2 - t1:0.4f} секунд\n")

"""Various Values"""
print('VARIOUS VALUES\n')
t1 = time.perf_counter()
print(has_duplicates(arrVarious))
t2 = time.perf_counter()
print(f"Вычисление заняло {t2 - t1:0.4f} секунд")

t1 = time.perf_counter()
print(get_duplicates(arrVarious))
t2 = time.perf_counter()
print(f"Вычисление заняло {t2 - t1:0.4f} секунд")
