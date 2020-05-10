"""
16:51 - 17:24
"""


def solve_case(ks):
    if ks[0] == 0 or ks[-1] == 0:
        return None
    blocks = []
    start = 0
    row_count = 0
    for target, dest in enumerate(ks):
        if dest > 0:
            end = start + dest
            blocks.append((target, start, end))
            row_count = max(abs(start - target), abs(end - 1 - target), row_count)
            start = end
    rows = []
    for _ in range(row_count + 1):
        rows.append(["."] * len(ks))

    for target, start, end in blocks:
        if target > start:
            for i in range(target - start):
                rows[-i - 2][target - i - 1] = "\\"
        if target < end - 1:
            for i in range(end - 1 - target):
                rows[-i - 2][target + i + 1] = "/"

    return rows


def print_soln(soln):
    if not soln:
        return "IMPOSSIBLE"
    return "{}\n{}".format(len(soln), "\n".join("".join(row) for row in soln))


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        input()
        ks = [int(x) for x in input().split(" ")]
        soln = solve_case(ks)
        print("Case #{}: {}".format(i, print_soln(soln)), flush=True)


if __name__ == "__main__":
    run()
