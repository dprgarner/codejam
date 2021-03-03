"""
Quick script to generate some golf holes for the wormhole problem.
"""

n = 5
print(n)
for _ in range(n):
    print(100)
    for i in range(10):
        for j in range(10):
            print("{} {}".format(i, 2 ** i + j))
