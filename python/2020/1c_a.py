"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/0000000000317409
"""


def solve_case(init_x, init_y, dirs):
    x, y = init_x, init_y
    for t in range(len(dirs) + 1):
        dist = abs(x) + abs(y)
        # print(dist, t)
        if dist <= t:
            return t
        if t < len(dirs):
            dir = dirs[t]
            if dir == 'N':
                y += 1
            elif dir == 'S':
                y -= 1
            elif dir == 'E':
                x += 1
            elif dir == 'W':
                x -= 1


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        x, y, dirs = input().split(' ')
        soln = solve_case(int(x), int(y), dirs) or 'IMPOSSIBLE'
        print('Case #{}: {}'.format(i, soln), flush=True)


if __name__ == '__main__':
    run()
