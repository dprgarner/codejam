"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9
"""


def solve_case(events):
    cs = []
    js = []
    # Fill C's and J's
    for (idx, s, e) in sorted(events, key=lambda x: x[1]):
        if cs and cs[-1][2] > s:
            # Add to J's, but check no clashes
            if js and js[-1][2] > s:
                return "IMPOSSIBLE"
            js.append((idx, s, e))
        else:
            cs.append((idx, s, e))

    partitioned = [(c[0], "C") for c in cs] + [(j[0], "J") for j in js]
    return "".join([z[1] for z in sorted(partitioned, key=lambda x: x[0])])


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n = int(input())
        events = []
        for k in range(n):
            events.append((k,) + tuple(int(x) for x in input().split(" ")))
        soln = solve_case(events)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
