"""

"""


def solve_case(ks):
    return ""


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        ks = (int(x) for x in input().split(" "))
        soln = solve_case(ks)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
