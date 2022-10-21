from main import Dictionary
import time
import random
import string


def randomWord():
    ran = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return str(ran)


N = int(input('Количество элементов: '))

d = Dictionary(N)
t1 = time.perf_counter()
for i in range(N):
    d.set(randomWord(), randomWord())
t2 = time.perf_counter()
print(f"Вставка: {t2 - t1:0.4f}")

t1 = time.perf_counter()
for i in range(1000):
    d.get(randomWord())
t2 = time.perf_counter()
print(f"Поиск: {t2 - t1:0.4f}")


print('Другая хэш функция:')


def hashF2(size, key):  # метод умножения
    sum = 0
    for i in key:
        sum += ord(i)
    return round(size * ((0.618 * sum) % 1))-1


d = Dictionary(N, hashF2)

t1 = time.perf_counter()
for i in range(N):
    d.set(randomWord(), randomWord())
t2 = time.perf_counter()
print(f"Вставка: {t2 - t1:0.4f}")

t1 = time.perf_counter()
for i in range(1000):
    d.get(randomWord())
t2 = time.perf_counter()
print(f"Поиск: {t2 - t1:0.4f}")


d = {}
print('Встроенный словарь')
t1 = time.perf_counter()
for i in range(N):
    d[randomWord()] = randomWord()
t2 = time.perf_counter()
print(f"Вставка: {t2 - t1:0.4f}")

t1 = time.perf_counter()
for i in range(1000):
    d.get(randomWord())
t2 = time.perf_counter()
print(f"Поиск: {t2 - t1:0.4f}")
