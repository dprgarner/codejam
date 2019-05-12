from random import random

t = 100
print(t)
n = 10000
k = 5000
l = 10000
for _ in range(t):
    print('{} {}'.format(n, k))
    print(' '.join(str(int(random() * l)) for _ in range(n)))
    print(' '.join(str(int(random() * l)) for _ in range(n)))
