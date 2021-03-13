"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146183
10:05-11:05.
Half of that time was spent debugging a bug caused by writing Fraction(x/y) instead of Fraction(x,y).
"""
from fractions import Fraction


def solve_case(molecules):
    ratios = set()
    for i, (c1, j1) in enumerate(molecules):
        for (c2, j2) in molecules[i + 1 :]:
            if (c1 > c2 and j1 < j2) or (c1 < c2 and j1 > j2):
                ratios.add(Fraction((c1 - c2), (j2 - j1)))

    return len(ratios) + 1


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n = int(input())
        molecules = []
        for _ in range(n):
            c, j = (int(x) for x in input().split(" "))
            molecules.append((c, j))
        soln = solve_case(molecules)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
