"""
S: 12:11ish
E: 12:44ish
"""


def solve_case(pats):
    # Common start of the stirng?
    starts = set()
    for x in pats:
        starts.add(x.split("*")[0])
    start = ""
    for x in sorted(starts):
        if not x.startswith(start):
            return "*"
        start = x
    # Common end of string?
    ends = set()
    for x in pats:
        ends.add("".join(reversed(x.split("*")[-1])))
    end = ""
    for x in sorted(ends):
        if not x.startswith(end):
            return "*"
        end = x
    end = "".join(reversed(end))

    # Any string containing all bits in patterns between the first and last star
    # will do.
    middles = []
    for pat in pats:
        s = pat.index("*")
        e = len(pat) - "".join(reversed(pat)).index("*")
        middles.append(pat[(s + 1) : (e - 1)].replace("*", ""))

    return "{}{}{}".format(start, "".join(middles), end)


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        pats = []
        for _ in range(int(input())):
            pats.append(input())
        soln = solve_case(pats)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
