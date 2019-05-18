"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146184
This just doesn't work. Oh well.
"""

import math


class ImpossibleException(Exception):
    pass


def get_ratio_range(ratios, pairs):
    ratios_extra = sorted(ratios, key=lambda x: x[0] / x[1])
    ratios_extra.insert(0, (0, 1))
    ratios_extra.append((1, 0))
    # print(ratios_extra)

    for (c1, j1), (c2, j2) in zip(ratios_extra, ratios_extra[1:]):
        mid_ratio = (
            None
            if j2 == 0
            else
            (c1 / j1 + c2 / j2) / 2
        )
        other_mid_ratio = (
            None
            if j2 == 0
            else
            (0.25 * c1 / j1 + 0.75 * c2 / j2)
        )
        last = 0
        bad_ratio = False
        for i in range(len(pairs)):
            c, j = pairs[i]
            trial1 = c + j * mid_ratio if mid_ratio != None else j
            trial2 = c + j * other_mid_ratio if other_mid_ratio != None else j
            if trial1 < last or trial2 < last:
                bad_ratio = True
                break
            last = trial1
        if not bad_ratio:
            return ((c1, j1), (c2, j2))

        # Try another one.
        last = 0
        bad_ratio = False
        for i in range(len(pairs)):
            c, j = pairs[i]
            trial = c + j * other_mid_ratio if other_mid_ratio != None else j
            if trial <= last:
                bad_ratio = True
                break
            last = trial
        if not bad_ratio:
            return ((c1, j1), (c2, j2))
    raise ImpossibleException


def bisect(start, end, lambda_):
    """
    Assuming that it exists, this function returns x in start <= x <= end s.t
    all([lambda[i] for i in range(start, x)]) == True
    any([lambda[i] for i in range(x, end)]) == False
    """
    assert start < end, '{} >= {}'.format(start, end)
    if start == end - 1:
        return end if lambda_(start) else start

    midpoint = (start + end) // 2
    if lambda_(midpoint):
        return bisect(midpoint, end, lambda_)
    else:
        return bisect(start, midpoint, lambda_)


def get_min_c_j(min_ratio, max_ratio):
    c_min, j_min = min_ratio
    c_max, j_max = max_ratio

    def get_c(i):
        # Any results between lines?
        upper = math.ceil(i * c_max / j_max) - 1
        lower = math.floor(i * c_min / j_min) + 1
        # print(i, upper, lower)
        # print(i, lower, upper, lower > upper)
        return lower > upper

    if j_max == 0:
        # print(min_ratio, max_ratio)
        return (1, math.floor(c_min / j_min) + 1)

    found_c = bisect(1, 1 + 10**9, get_c)
    calced_j = math.floor(c_min * found_c / j_min) + 1
    return (found_c, calced_j)


def solve_case(pairs):
    ratios = set()
    for (c1, j1), (c2, j2) in zip(pairs, pairs[1:]):
        if c1 >= c2 and j1 >= j2:
            raise ImpossibleException
        if c1 < c2 and j1 > j2 or c1 > c2 and j1 < j2:
            # print(c1, c2, j1, j2)
            divisor = math.gcd(abs(c2 - c1), abs(j1 - j2))
            a = (c2 - c1) // divisor
            b = (j1 - j2) // divisor
            ratios.add((a, b) if a > 0 else (-a, -b))

    min_ratio, max_ratio = get_ratio_range(ratios, pairs)

    cw, jw = get_min_c_j(min_ratio, max_ratio)
    last = 0
    for c, j in pairs:
        assert c * cw + j * jw > last
        last = c * cw + j * jw

    # print(min_ratio, max_ratio)
    return '{} {}'.format(cw, jw)


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n = int(input())
        pairs = []
        for _ in range(n):
            c, j = (int(x) for x in input().split(' '))
            pairs.append((c, j))
        try:
            soln = solve_case(pairs)
        except ImpossibleException:
            soln = 'IMPOSSIBLE'
        print('Case #{}: {}'.format(i, soln), flush=True)


if __name__ == '__main__':
    run()
