"""
Helper script for creating test cases.
"""

import random


t = 100000

print(t)
for _ in range(t):
    n = random.choice(range(2, 10 + 1))
    print(n)
    for _ in range(n):
        c = random.choice(range(1, 10))
        j = random.choice(range(1, 10))
        print('{} {}'.format(c, j))
