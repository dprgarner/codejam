"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146184
11:18
12:36
"""
from fractions import Fraction
from math import inf, ceil


def bisect(start, end, lambda_):
    """
    Assuming that it exists, this function returns x in start <= x <= end s.t
    all([lambda[i] for i in range(start, x)]) == True
    any([lambda[i] for i in range(x, end)]) == False
    In particular, lambda[x] == False.
    """
    assert start < end, "{} >= {}".format(start, end)
    if start == end - 1:
        return end if lambda_(start) else start

    midpoint = (start + end) // 2
    if lambda_(midpoint):
        return bisect(midpoint, end, lambda_)
    else:
        return bisect(start, midpoint, lambda_)


def solve_case(molecules):
    ratios = []
    upper = inf
    lower = 0

    for (c1, j1), (c2, j2) in zip(molecules, molecules[1:]):
        if j1 > j2 and c1 < c2:
            upper = min(upper, Fraction((c1 - c2), (j2 - j1)))
        elif j1 < j2 and c1 > c2:
            lower = max(lower, Fraction((c1 - c2), (j2 - j1)))
        elif j1 >= j2 and c1 >= c2:
            return None

    if lower >= upper:
        return None

    if upper == inf:
        c = 1
        j = ceil(lower)
        if j == lower:
            j += 1
        return (c, j)

    target = Fraction(lower + upper, 2)

    def is_in_range(c):
        truncated = target.limit_denominator(c)
        return truncated < upper and truncated > lower

    c = bisect(1, target.denominator, lambda c: not is_in_range(c))

    max_j = target.limit_denominator(c).numerator
    j = bisect(0, max_j + 1, lambda j: Fraction(j, c) <= lower)

    return c, j


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n = int(input())
        molecules = []
        for _ in range(n):
            c, j = (int(x) for x in input().split(" "))
            molecules.append((c, j))
        soln = solve_case(molecules)
        if soln:
            soln_str = "{} {}".format(*soln)
        else:
            soln_str = "IMPOSSIBLE"
        print("Case #{}: {}".format(i, soln_str), flush=True)


if __name__ == "__main__":
    run()
