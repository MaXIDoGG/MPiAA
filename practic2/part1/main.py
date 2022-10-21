from count_sort import counting_sort
from random import randint
import time


N = int(input('Количество элементов: '))
arr = [0]*N
for i in range(0, N):
    random_count = randint(-N, N)
    arr[i] = random_count

t1 = time.perf_counter()
arr = counting_sort(arr)
t2 = time.perf_counter()
print(f"Время работы сортировки подсчётом: {t2 - t1:0.6f} секунд.")
print("=======")

t1 = time.perf_counter()
arr.sort()
t2 = time.perf_counter()
print(f"Время работы сортировки .sort(): {t2 - t1:0.6f} секунд.")
