import sys

n = 0

candidates = [(x, y) for x in range(1, 10) for y in range(1, 10)]
print(len(candidates))
for x, y in candidates:
    print("{} {}".format(x, y))
