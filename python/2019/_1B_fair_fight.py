"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122838
Works on the small set, still too slow for the large set.
"""


class MaxRangeTree:
    compare = max

    def __init__(self, array, start=None, end=None):
        self.array = array
        assert array, 'Array must be non-empty'
        self.start = 0 if start == None else start
        self.end = len(array) if end == None else end
        self.set_tree()

    def set_tree(self):
        if self.start == self.end - 1:
            self.value = self.array[self.start]
        else:
            midpoint = (self.start + self.end) // 2
            self.left = self.__class__(self.array, self.start, midpoint)
            self.right = self.__class__(self.array, midpoint, self.end)
            self.value = self.compare(self.left.value, self.right.value)

    def rmq(self, start, end):
        assert start < end, '{} >= {}'.format(start, end)
        if self.start == start and self.end == end:
            return self.value

        if start >= self.right.start:
            return self.right.rmq(start, end)

        if end <= self.left.end:
            return self.left.rmq(start, end)

        return self.compare(
            self.left.rmq(start, self.left.end),
            self.right.rmq(self.right.start, end)
        )


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


def solve_case(cs, ds, k):
    count = 0
    return 0
    n = len(cs)
    for i in range(n):
        max_cap = cs[i] + k + 1
        min_cap = cs[i] - k
        if ds[i] < max_cap:
            count += get_capped_pairs_count(
                n, i, cs, ds, max_cap
            )
        if ds[i] < min_cap:
            count -= get_capped_pairs_count(
                n, i,  cs, ds, min_cap
            )
    return count


def main():
    cases = int(input())
    for i in range(1, cases + 1):
        n, k = (int(x) for x in input().split(' '))
        cs = [int(x) for x in input().split(' ')]
        ds = [int(x) for x in input().split(' ')]
        soln = solve_case(cs, ds, k)
        print('Case #{}: {}'.format(i, soln), flush=True)


if __name__ == '__main__':
    main()
