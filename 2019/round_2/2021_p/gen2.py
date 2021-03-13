from random import randint

t = 1000000

print(t)
for _ in range(t):
    case = []
    n = randint(1, 10)
    for _ in range(n):
        case.append((randint(1, 10 ** 4), randint(1, 10 ** 4)))
    print(len(case))
    for c, j in case:
        print("{} {}".format(c, j))
