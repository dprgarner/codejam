"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122838
Works on the small set, still too slow for the large set.
"""


def get_capped_pairs_count(i, c_lower, c_upper, ds, cap):
    # What range is Max(ds[a:b]) < cap, where a <= i <= b?
    if ds[i] >= cap:
        return 0

    d_lower = i
    while d_lower > c_lower and ds[d_lower] < cap:
        d_lower -= 1
    if ds[d_lower] >= cap:
        d_lower += 1

    d_upper = i + 1
    while d_upper < c_upper and ds[d_upper - 1] < cap:
        d_upper += 1
    if ds[d_upper - 1] >= cap:
        d_upper -= 1

    count = (1 + i - d_lower) * (d_upper - i)
    return count


def solve_case(cs, ds, k):
    n = len(cs)
    count = 0

    for i in range(n):
        c_lower = i - 1
        # For what range is cs[i] the biggest c?
        while c_lower >= 0 and cs[i] > cs[c_lower]:
            c_lower -= 1
        c_lower += 1
        c_upper = i + 1
        while c_upper < n and cs[i] >= cs[c_upper]:
            c_upper += 1

        count += get_capped_pairs_count(i, c_lower, c_upper, ds, cs[i] + k + 1)
        count -= get_capped_pairs_count(i, c_lower, c_upper, ds, cs[i] - k)
    return count


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n, k = (int(x) for x in input().split(' '))
        cs = [int(x) for x in input().split(' ')]
        ds = [int(x) for x in input().split(' ')]
        soln = solve_case(cs, ds, k)
        print('Case #{}: {}'.format(i, soln), flush=True)


if __name__ == '__main__':
    run()
