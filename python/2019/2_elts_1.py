"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146183
This one worked.
"""

import math


def solve_case(pairs):
    ratios = set()
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            c1, j1 = pairs[i]
            c2, j2 = pairs[j]
            if c1 > c2 and j1 < j2 or c1 < c2 and j1 > j2:
                # These pairs can be in either order: record ratio
                divisor = math.gcd(abs(c2 - c1), abs(j1 - j2))
                a = (c2 - c1) // divisor
                b = (j1 - j2) // divisor
                ratios.add((a, b) if a > 0 else (-a, -b))
                # print(c1, j1, '-', c2, j2)
    # print(ratios)
    return len(ratios) + 1


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n = int(input())
        pairs = []
        for _ in range(n):
            c, j = (int(x) for x in input().split(' '))
            pairs.append((c, j))
        soln = solve_case(pairs)
        print('Case #{}: {}'.format(i, soln), flush=True)


if __name__ == '__main__':
    run()
