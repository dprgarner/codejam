"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019ffb9/00000000003384ea
Re-attempt.
11:05
14:02. Fucking hell.
"""
from math import floor


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


def consecutive_sum(x):
    return x * (x + 1) // 2


def step_two_sum(n, m):
    # n + (n+2) + (n+4) + ... + m, where m, n are same parity
    assert (n - m) % 2 == 0
    if n % 2 == 0 and m % 2 == 0:
        return (m // 2) * (1 + m // 2) - ((n - 1) // 2) * (1 + (n - 1) // 2)

    if n % 2 == 1 and m % 2 == 1:
        return ((m + 1) // 2) ** 2 - ((n - 1) // 2) ** 2


def solve_case(l, r):
    swapped = False
    n = 0

    if l < r:
        swapped = not swapped
        l, r = r, l

    if l == r:
        d = 0
    else:
        d = bisect(0, l - r + 1, lambda x: consecutive_sum(x) <= l - r) - 1
        assert consecutive_sum(d) <= l

    l -= consecutive_sum(d)
    n += d

    if l < r:
        swapped = not swapped
        l, r = r, l
    elif l == r and swapped:
        swapped = not swapped
        l, r = r, l

    assert l >= 0
    assert r >= 0
    assert l >= r
    assert l - (n + 1) < r

    # How many from L?
    if n + 1 > l:
        x = 0
    elif n + 1 == l:
        x = 1
        l -= n + 1
    else:
        x = bisect(1, l + 1, lambda x: step_two_sum(n + 1, n - 1 + 2 * x) <= l) - 1
        l -= step_two_sum(n + 1, n - 1 + 2 * x)

    # How many from R?
    if n + 2 > r:
        y = 0
    elif n + 2 == r:
        y = 1
        r -= n + 2
    else:
        y = bisect(1, r + 1, lambda y: step_two_sum(n + 2, n + 2 * y) <= r) - 1
        r -= step_two_sum(n + 2, n + 2 * y)

    assert l >= 0
    assert r >= 0
    n = max(n - 1 + 2 * x, n + 2 * y)

    return (n, r, l) if swapped else (n, l, r)


def check(l, r):
    """
    Too slow for large dataset. Used for checking.
    """
    n = 1
    while l >= 0 or r >= 0:
        if l >= r and l >= n:
            l -= n
            n += 1
        elif l < r and r >= n:
            r -= n
            n += 1
        else:
            break
    return (n - 1), l, r


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        l, r = (int(x) for x in input().split(" "))
        soln = solve_case(l, r)
        # assert soln == check(l, r), "Not equal: {} {} {}  -- {} {} {}".format(
        #     *soln, *check(l, r)
        # )
        print("Case #{}: {} {} {}".format(i, *soln), flush=True)


if __name__ == "__main__":
    run()
