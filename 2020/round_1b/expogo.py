"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62
No idea what went wrong here. Something's giving a non-minimal answer, or saying
it's impossible when it's not.
"""


def expand(x):
    if x == 0:
        return ((0, 0),)
    digits = "{0:b}".format(abs(x))
    d = len(digits)
    solns = []

    solns.append((abs(x), 0) if x > 0 else (0, abs(x)))

    for i in range(0, 30):
        candidate_diff = abs(abs(x) - 2 ** i)
        # Share a digit?
        # print("{0:b} {1:b}".format(candidate_diff, 2 ** i))
        # print(2 ** i, candidate_diff)
        solns.append((2 ** i, candidate_diff) if x > 0 else (candidate_diff, 2 ** i))

    # for a, b in solns:
    #     assert a - b == x, (a, b, x)

    return ((a, b) for a, b in solns if a - b == x)
    # return solns


def to_str(p1, n1, p2, n2):
    ns = "{0:b}".format(p2)
    ss = "{0:b}".format(n2)
    es = "{0:b}".format(p1)
    ws = "{0:b}".format(n1)
    digits = max(len(dir_) for dir_ in (ns, es, ss, ws))
    while len(ns) < digits:
        ns = "0" + ns
    while len(ss) < digits:
        ss = "0" + ss
    while len(es) < digits:
        es = "0" + es
    while len(ws) < digits:
        ws = "0" + ws

    # raise Exception(ns, es, ss, ws)
    # print(digits)
    str_ = []
    for i in range(-1, -digits - 1, -1):
        # print(i)
        if ns[i] == "1":
            str_.append("N")
        elif ss[i] == "1":
            str_.append("S")
        elif es[i] == "1":
            str_.append("E")
        if ws[i] == "1":
            str_.append("W")
    # print(str_)
    return "".join(str_)


def solve_case(x, y):
    combs = [(a, b) for a in expand(x) for b in expand(y)]

    min_sol = None
    for ((p1, n1), (p2, n2)) in combs:
        if all(c == "1" for c in "{0:b}".format(p1 + p2 + n1 + n2)):
            # It's a soln.
            sol = to_str(p1, n1, p2, n2)
            # check(sol, x, y)
            if not min_sol or len(sol) < len(min_sol):
                # It's minimal
                min_sol = sol

    return min_sol or "IMPOSSIBLE"

    # print("{0:b} {1:b} {2:b} {3:b}".format(*min_sol))


def check(str_, realx, realy):
    x, y = (0, 0)
    if str_ == "IMPOSSIBLE":
        return
    for i, c in enumerate(str_):
        if c == "N":
            y = y + 2 ** i
        if c == "S":
            y = y - 2 ** i
        if c == "E":
            x = x + 2 ** i
        if c == "W":
            x = x - 2 ** i
    assert (x, y) == (realx, realy), (x, y)


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        x, y = (int(x) for x in input().split(" "))
        soln = solve_case(x, y)
        print("Case #{}: {}".format(i, soln), flush=True)
        check(soln, x, y)


if __name__ == "__main__":
    run()
