"""
https://code.google.com/codejam/contest/8294486/dashboard#s=p1
Done for practice. ~1h.
"""

IMPOSSIBLE = "IMPOSSIBLE"


def solve_case(_n, r, o, y, g, b, v):
    # Special cases: alternating rings
    if g and g == r:
        if any([o, y, b, v]):
            return IMPOSSIBLE
        return "GR" * r
    if v and v == y:
        if any([r, o, g, b]):
            return IMPOSSIBLE
        return "VY" * y
    if o and o == b:
        if any([r, y, g, v]):
            return IMPOSSIBLE
        return "OB" * b

    # Secondaries need to be totally surrounded by opposite primary colour
    if r < g or y < v or b < o:
        return IMPOSSIBLE

    # Insert BOBOB/RGRGR/YVYVY string at end
    r = r - g
    y = y - v
    b = b - o

    s = r + y + b - 2 * max(r, y, b)
    if s < 0:
        return IMPOSSIBLE

    # Must be a soln
    if r == max(r, y, b):
        ans = ("RYB" * s) + ("RB" * (r - y)) + ("RY" * (r - b))
    elif y == max(r, y, b):
        ans = ("YBR" * s) + ("YB" * (y - r)) + ("YR" * (y - b))
    else:
        ans = ("BRY" * s) + ("BY" * (b - r)) + ("BR" * (b - y))

    if g:
        idx = ans.index("R")
        ans = ans[: idx + 1] + ("GR" * g) + ans[idx + 1 :]
    if v:
        idx = ans.index("Y")
        ans = ans[: idx + 1] + ("VY" * v) + ans[idx + 1 :]
    if o:
        idx = ans.index("B")
        ans = ans[: idx + 1] + ("OB" * o) + ans[idx + 1 :]

    return ans


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        ks = (int(x) for x in input().split(" "))
        soln = solve_case(*ks)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
