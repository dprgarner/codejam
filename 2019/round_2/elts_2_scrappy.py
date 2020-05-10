"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146184
Brute force method. Only works for the small case.
"""


class ImpossibleException(Exception):
    pass


def check(pairs, cw, jw):
    last = 0
    for c, j in pairs:
        if cw < 6 and jw < 6:
            # print('try: ', cw, jw, 'on:', c, j)
            # print('last:', last)
            # print('now:', c * cw + j * jw)
            if c * cw + j * jw <= last:
                pass
                # print('not strictly increasing')
            else:
                pass
                # print('so far so good')
                # if c > 100 or j > 100:
                #     raise Exception('nope')
        if c * cw + j * jw <= last:
            return False
        last = c * cw + j * jw
    # print('ok')
    return True


def solve_small_case(pairs):
    for c in range(1, 200):
        for j in range(1, 200):
            if check(pairs, c, j):
                return '{} {}'.format(c, j)
    raise ImpossibleException


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n = int(input())
        pairs = []
        for _ in range(n):
            c, j = (int(x) for x in input().split(' '))
            pairs.append((c, j))
        try:
            # Smaller version.
            soln = solve_small_case(pairs)
        except ImpossibleException:
            soln = 'IMPOSSIBLE'
        print('Case #{}: {}'.format(i, soln), flush=True)


if __name__ == '__main__':
    run()
