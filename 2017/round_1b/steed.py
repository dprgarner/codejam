"""

"""


def solve_case(distance, horses):
    max_time = 0
    for d1, s1 in horses:
        max_time = max(max_time, (distance - d1) / s1)
    return distance / max_time


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        d, h = (int(x) for x in input().split(" "))
        horses = []
        for _ in range(h):
            horses.append(tuple(int(x) for x in input().split(" ")))
        soln = solve_case(d, horses)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
