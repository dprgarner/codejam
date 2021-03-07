"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019ffb9/00000000003384ea
13:45-14:18.
"""


def bisect(start, end, lambda_):
    """
    Assuming that it exists, this function returns x in start <= x <= end s.t
    all([lambda[i] for i in range(start, x)]) == True
    any([lambda[i] for i in range(x, end)]) == False
    """
    assert start < end, "{} >= {}".format(start, end)
    if start == end - 1:
        return end if lambda_(start) else start

    midpoint = (start + end) // 2
    if lambda_(midpoint):
        return bisect(midpoint, end, lambda_)
    else:
        return bisect(start, midpoint, lambda_)


def solve_case(l, r):
    swapped = False
    if l < r:
        swapped = True
        l, r = r, l

    # How many customers take from l in a row to start?
    d = bisect(0, l - r + 1, lambda x: x * (x + 1) // 2 <= (l - r)) - 1

    l -= d * (d + 1) // 2
    if swapped:
        l, r = r, l
    swapped = False

    # Set it up to take from the left first
    if l < r:
        swapped = True
        l, r = r, l

    c1 = bisect(0, l + 1, lambda x: (x) * (x + d) <= l) - 1
    l -= c1 * (c1 + d)

    c2 = bisect(0, r + 1, lambda x: (x) * (x + d + 1) <= r) - 1
    r -= c2 * (c2 + d + 1)

    if swapped:
        l, r = r, l

    return d + c1 + c2, l, r


def check(l, r):
    n = 0
    while True:
        n += 1
        if l >= r and l >= n:
            l -= n
        elif r >= n:
            r -= n
        else:
            return n - 1, l, r


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        l, r = (int(x) for x in input().split(" "))
        soln = solve_case(l, r)
        # assert soln == check(l, r), "{} {}".format(l, r)
        print("Case #{}: {} {} {}".format(i, *soln), flush=True)


if __name__ == "__main__":
    run()
