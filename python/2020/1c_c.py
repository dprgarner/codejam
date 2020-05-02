"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003172d1
Somewhat scrappy solution to just the first part.
"""


def solve_case(diners, slices):
    if diners == 2:
        for i in range(len(slices) - 1):
            if slices[i] == slices[i + 1]:
                return 0
        return 1

    #diners == 3
    uniq = set(slices)
    poss_1 = False
    for i in range(len(slices) - 2):
        if slices[i] == slices[i+1] and slices[i+1] == slices[i+2]:
            return 0
        elif slices[i] == slices[i+1]:
            poss_1 = True
    if poss_1:
        return 1
    # ...?

    for i in range(len(slices)):
        for j in range(i, len(slices)):
            if slices[i] + slices[j] in uniq:
                return 1
    return 2

    # print(diners, slices)
    return '?#'


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n, d = (int(x) for x in input().split(' '))
        slices = [int(x) for x in input().split(' ')]
        # assert len(slices) == n
        if d > 3:
            raise Exception('no idea')
        slices.sort()
        soln = solve_case(d, slices)
        print('Case #{}: {}'.format(i, soln), flush=True)


if __name__ == '__main__':
    run()

"""
3: 1
2: 10 5 359999999999 123456789 10
3: 8 4
2: 1 2 3
"""
