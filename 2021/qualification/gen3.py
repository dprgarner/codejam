t = 0
max_n = 100
egs = []

for n in range(2, max_n):
    for c in range(1, n * n):
        egs.append("{} {}".format(n, c))

print(len(egs))
for eg in egs:
    print(eg)
