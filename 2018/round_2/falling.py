"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000007706/00000000000459f2
"""


def solve(bs):
    if bs[0] == 0 or bs[-1] == 0:
        return

    balls_falling_in_col = []
    total = 0
    max_diff = 0
    for i, b in enumerate(bs):
        balls_falling_in_col.append((total, total + b))
        max_diff = max([max_diff, (i - total), (total + b - 1 - i)])
        total += b

    grid = []
    for _ in range(max_diff):
        grid.append(['.'] * len(bs))

    for i, (start, end) in enumerate(balls_falling_in_col):
        x = 0
        while start + x < i:
            grid[x][start + x] = '\\'
            x += 1

        x = 0
        while end - 1 - x > i:
            grid[x][end - 1 - x] = '/'
            x += 1

    grid.append(['.'] * len(bs))
    return grid


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        c = int(input())
        bs = [int(x) for x in input().split(' ')]
        soln = solve(bs)
        if soln:
            print('Case #{}: {}\n{}'.format(
                i,
                len(soln),
                '\n'.join(''.join(row) for row in soln)
            ), flush=True)
        else:
            print('Case #{}: IMPOSSIBLE'.format(i), flush=True)


if __name__ == '__main__':
    run()
