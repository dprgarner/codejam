"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007549e5
30m
"""


def solve_case(ks):
    n = len(ks)
    appended_digits = 0
    for idx in range(n - 1):
        i, j = ks[idx], ks[idx + 1]
        if i == j:
            # Just add a single zero.
            appended_digits += 1
            ks[idx + 1] *= 10
        elif i > j:
            # Try and find smallest number greater than i that starts with
            # digits of j
            if str(i + 1).startswith(str(j)):
                new_digits = len(str(i + 1)) - len(str(j))
                ks[idx + 1] = i + 1
                appended_digits += new_digits
            else:
                # No such number, so wrap to the next power of 10 larger than i
                zeroes = len(str(i)) - len(str(j))
                ks[idx + 1] = j * 10 ** zeroes
                if ks[idx + 1] < i:
                    ks[idx + 1] *= 10
                    zeroes += 1
                appended_digits += zeroes
    return appended_digits


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        input()
        ks = list(int(x) for x in input().split(" "))
        soln = solve_case(ks)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
