import math
from fractions import Fraction
"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146184
"""


class ImpossibleException(Exception):
    pass


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


def get_min_j_over_c(min_ratio, max_ratio):
    lower = Fraction(max_ratio[1], max_ratio[0])
    if min_ratio[0] == 0:
        # print(min_ratio, max_ratio)
        # C =1, J is the biggest int over lower
        return Fraction(math.floor(lower) + 1, 1)

    upper = Fraction(min_ratio[1], min_ratio[0])
    # print(min_ratio, max_ratio)
    # min_ratio[0] / min_ratio[1] < C/J < max_ratio[0] / max_ratio[1]
    # lower < J/C < upper

    midpoint = (lower + upper) / 2

    def try_c(c):
        approx = Fraction.limit_denominator(midpoint, c)
        # print(c, approx, (lower < approx and upper > approx))
        return not (lower < approx and upper > approx)

    y = bisect(1, 10**10 + 1, try_c)
    x = math.floor(lower * y) + 1
    return Fraction(x, y)


def solve_case(pairs):
    min_ratio = None
    max_ratio = None
    for (c1, j1), (c2, j2) in zip(pairs, pairs[1:]):
        if c1 >= c2 and j1 >= j2:
            raise ImpossibleException
        if c1 < c2 and j1 > j2 and (
            not min_ratio or
            (j1 - j2) * min_ratio[1] > min_ratio[0] * (c2 - c1)
        ):
            min_ratio = (j1 - j2, c2 - c1)
            # print('min', min_ratio)

        if c1 > c2 and j1 < j2 and (
            not max_ratio or
            (j2 - j1) * max_ratio[1] < max_ratio[0] * (c1 - c2)
        ):
            max_ratio = (j2 - j1, c1 - c2)
            # print('max', max_ratio)

    # min_ratio < C/J < max_ratio
    if (
        min_ratio and max_ratio and
        min_ratio[0] * max_ratio[1] >= max_ratio[0] * min_ratio[1]
    ):
        raise ImpossibleException

    frac = get_min_j_over_c(min_ratio or (0, 1), max_ratio or (1, 0))
    jw, cw = frac.numerator, frac.denominator
    # print('found:', cw, jw)
    last = 0
    for c, j in pairs:
        assert c * cw + j * jw > last, pairs
        last = c * cw + j * jw

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
