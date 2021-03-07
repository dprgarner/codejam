cases = []
for i in range(1, 10):
    for j in range(1, 10):
        cases.append((i, j))

print(len(cases))
for i, j in cases:
    print("{} {}".format(i, j))
