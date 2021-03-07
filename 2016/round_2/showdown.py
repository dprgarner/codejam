"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000201c91/0000000000201d1e
14:25- 15:17
"""


def soln_sort(pairs):
    n = len(pairs) // 2
    if n <= 1:
        return "".join(sorted(pairs))
    return "".join(sorted([soln_sort(pairs[0:n]), soln_sort(pairs[n:])]))


def build_next_level(str_):
    new_str = []
    for c in str_:
        if c == "R":
            new_str.append("RS")
        if c == "P":
            new_str.append("PR")
        if c == "S":
            new_str.append("PS")

    return soln_sort(new_str)


def count_chars(str_):
    r, p, s = 0, 0, 0
    for c in str_:
        if c == "R":
            r += 1
        if c == "P":
            p += 1
        if c == "S":
            s += 1
    return (r, p, s)


def build_tables(n):
    tables = {}
    for s in ["R", "P", "S"]:
        while len(s) < 2 ** n:
            count = count_chars(s)
            tables[count] = s
            s = build_next_level(s)
    return tables


def run():
    tables = build_tables(14)
    # for k, v in tables.items():
    #     print(k, v)
    cases = int(input())
    for i in range(1, cases + 1):
        n, r, p, s = (int(x) for x in input().split(" "))
        soln = tables.get((r, p, s), "IMPOSSIBLE")
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
