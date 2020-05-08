sols = []
for i in range(-100, 101):
    for j in range(-100, 101):
        sols.append((i, j))
print(len(sols))
for (i, j) in sols:
    print("{} {}".format(i, j))
