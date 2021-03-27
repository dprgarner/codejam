"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
"""
from math import inf


# def check_case(ls):
#     n = len(ls)
#     cost = 0
#     for i in range(0, n - 1):
#         j = -1
#         min_j = inf
#         for k in range(i, n):
#             if ls[k] < min_j:
#                 j = k
#                 min_j = ls[k]

#         xs = list(reversed(ls[i : j + 1]))
#         cost += j - i + 1
#         for k, v in enumerate(xs):
#             ls[i + k] = v
#     return cost


def solve_case(n, c):
    if c < n - 1 or c > (n * (n + 1) // 2 - 1):
        return None

    c -= n - 1
    ls = []

    i = 0
    while c > n - i - 1:
        ls.insert(len(ls) // 2, i + 1)
        c -= n - i - 1
        i += 1

    # ls.insert(len(ls) // 2, None)
    should_reverse = len(ls) % 2 == 1

    to_insert = list(range(i + 1, n - c)) + list(reversed(range(n - c, n + 1)))

    if should_reverse:
        return ls[: len(ls) // 2] + list(reversed(to_insert)) + ls[len(ls) // 2 :]
    else:
        return ls[: len(ls) // 2] + to_insert + ls[len(ls) // 2 :]


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n, c = (int(x) for x in input().split(" "))
        soln = solve_case(n, c)
        if soln:
            soln_str = " ".join(str(s) for s in soln)
            # actual_c = check_case(soln)
            # assert actual_c == c, (soln_str, c, actual_c)
        else:
            soln_str = "IMPOSSIBLE"

        print("Case #{}: {}".format(i, soln_str), flush=True)


if __name__ == "__main__":
    run()
