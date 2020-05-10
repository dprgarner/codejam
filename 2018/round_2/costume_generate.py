from random import randint

t = 50
max_n = 100
print(t)
for _ in range(t):
    n = randint(2, max_n)
    print(n)
    for _ in range(n):
        row = [randint(1, n) * (2 * randint(0, 1) - 1) for _ in range(n)]
        print(" ".join(str(c) for c in row))
