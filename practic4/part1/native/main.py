from func import nativeLcs
import time
import random
import string

letters = string.ascii_lowercase + string.ascii_uppercase + \
    string.digits + string.punctuation

N = int(input('N = '))
M = int(input('M = '))
x = ''
y = ''

for i in range(N):
    x += random.choice(letters)
for i in range(M):
    y += random.choice(letters)

t1 = time.perf_counter()
LCS = nativeLcs(x, y)
t2 = time.perf_counter()

print(str(LCS), f"Время: {t2 - t1:0.4f}")
