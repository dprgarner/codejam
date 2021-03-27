"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
"""
from math import inf


def solve_case(ls):
    n = len(ls)
    cost = 0
    for i in range(0, n - 1):
        j = -1
        min_j = inf
        for k in range(i, n):
            if ls[k] < min_j:
                j = k
                min_j = ls[k]

        xs = list(reversed(ls[i : j + 1]))
        cost += j - i + 1
        for k, v in enumerate(xs):
            ls[i + k] = v
        print(ls)
    return cost


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        input()
        ls = list(int(x) for x in input().split(" "))
        soln = solve_case(ls)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
