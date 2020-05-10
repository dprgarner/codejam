"""
12:45ish
13:43. Woo!
"""


def binomial(n, k):
    num = 1
    for x in range(n - k + 1, n + 1):
        num *= x
    denom = 1
    for x in range(1, k + 1):
        denom *= x
    return num // denom


def check_route(route):
    s = 0
    for (n, k) in route:
        s += binomial(n, k)
    return s


def solve_case(total):
    """
    0-indexed.
    """
    if total < 31:
        return [(i, 0) for i in range(total)]

    # Each row sums to 2*r
    expansion = "{0:b}".format(total - 30)
    rows_to_add = [digit == "1" for digit in reversed(expansion)]
    while len(rows_to_add) < 30:
        rows_to_add.append(False)

    entries = []
    on_left = True
    for i, include_row in enumerate(rows_to_add):
        if include_row:
            entries_in_row = range(i + 1) if on_left else range(i, -1, -1)
            for k in entries_in_row:
                entries.append((i, k))
            on_left = not on_left
        else:
            entries.append((i, 0 if on_left else i))

    remaining = total - check_route(entries)
    for i in range(30, 30 + remaining):
        entries.append((i, 0 if on_left else i))
    return entries


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        k = int(input())
        soln = solve_case(k)
        assert k == check_route(soln), (k, soln, check_route(soln))
        assert len(soln) < 500
        print(
            "Case #{}:\n{}".format(
                i, "\n".join("{} {}".format(i + 1, j + 1) for (i, j) in soln)
            ),
            flush=True,
        )


if __name__ == "__main__":
    run()
