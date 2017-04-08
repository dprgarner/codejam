from codejam import CodeJamParser
from math import log2


"""
When a person occupies a "block" (consecutive set of unoccupied stalls),
the block is divided into two parts, which differ in size by zero or one.

Given a number of stalls, we can draw a binary tree of the sizes of the
blocks and their consecutive dividings. As, within each level, the sizes of the
blocks can only differ by at most one, we can calculate iteratively
in logarithmic time the size of the block that the kth person will enter.
From this, we can read off the values of max {max(L_s, R_s)} and
max {min(L_s, R_s)}.
"""


def get_level(k):
    """
    The kth person to enter the bathroom will pick a stall on this 'level',
    with levels starting from zero.
    If there are 2^(n-1) <= N < 2^n bathrooms, then there are n levels.
    """
    return int(log2(k))


def get_next_level(c, p, q):
    """
    If a 'level' has p blocks of stalls of size c and q blocks of stalls of
    size c+1, then what is the value of c, p, q for the next level?
    """
    return (
        (int(c / 2) - 1, p, p + 2 * q)
        if c % 2 == 0
        else (int((c - 1) / 2), 2 * p + q, q)
    )


def get_level_profile(n, l):
    """
    Get respective stall sizes and numbers for level l, when there are n stalls.
    """
    c, p, q = (n, 1, 0)
    for i in range(l):
        c, p, q = get_next_level(c, p, q)
    return (c, p, q)


def get_position(k):
    """
    Returns (l, r), where l is the level and r is the position in the level.
    """
    l = get_level(k)
    return (l, k - 2**l)


def get_block_size(n, k):
    """
    The size of the block (set of consecutive unoccupied stalls)
    that the kth person enters.
    """
    l, r = get_position(k)
    c, p, q = get_level_profile(n, l)
    return c + 1 if r < q else c


def get_max_min(block_size):
    """
    Given the size of a block that the person has occupied, find the
    required values of max {max(L_s, R_s)} and max {min(L_s, R_s)}.
    """
    return (int(block_size / 2), int((block_size - 1) / 2))


def _handle_case(stalls, people):
    max_, min_ = get_max_min(get_block_size(stalls, people))
    return '{} {}'.format(str(max_), str(min_))


class Stalls(CodeJamParser):
    """
    2017, Qualification round, C
    https://code.google.com/codejam/contest/3264486/dashboard#s=p2
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            case_line = next(self.source)
            stalls, people = case_line.split(' ')
            yield int(stalls), int(people)

    def handle_case(self, stalls, people):
        return _handle_case(stalls, people)


if __name__ == '__main__':
    Stalls()