"""
Didn't work. No idea why. Probably a rounding error when doing the square root.
"""


import random
import math


def triangle(x):
    return x * (x + 1) // 2


# print([triangle(i) for i in range(10)])


def invert_triangle(x):
    return math.floor((math.sqrt(1 + 8 * x) - 1) // 2)


def formula(k, t):
    return math.floor((math.sqrt(
        (k-1)**2 + 4*t
    ) - (k-1)) // 2)


def solve_case(l, r):
    initial_l, initial_r = l, r
    # print('---')
    print('initial:', initial_l, initial_r)
    # print('---')
    ls = []
    rs = []
    swapped = l < r
    if swapped:
        l, r = r, l
    # print((l, r))

    taken_from_left = invert_triangle(l - r)
    i = taken_from_left
    l -= triangle(i)

    if swapped and l == r:
        l, r = r, l
        swapped = False

    # print('***')
    # print((i, ':', l, r))
    max_i_can_take_from_l = formula(i+1, l)
    max_i_can_take_from_r = formula(i+2, r)
    # print('fomrulae:', max_i_can_take_from_l, max_i_can_take_from_r)
    max_i_can_take_from_r = min(max_i_can_take_from_l, max_i_can_take_from_r)
    max_i_can_take_from_l = min(
        max_i_can_take_from_l,
        max_i_can_take_from_r + 1
    )
    # print('take number:', max_i_can_take_from_l, max_i_can_take_from_r)
    take_from_l = max_i_can_take_from_l * (max_i_can_take_from_l + i)
    take_from_r = max_i_can_take_from_r * (max_i_can_take_from_r + i + 1)

    # print('take value:', take_from_l, take_from_r)

    l -= take_from_l
    r -= take_from_r
    i += max_i_can_take_from_l
    i += max_i_can_take_from_r
    s = (i, r, l) if swapped else (i, l, r)

    assert s[1] >= 0, s
    assert s[2] >= 0, s
    # check
    # l, r = initial_l, initial_r
    # for j in range(1, i + 1):
    #     if initial_l >= j and initial_l >= initial_r:
    #         initial_l -= j
    #     elif initial_r >= j and initial_r > initial_l:
    #         initial_r -= j
    #     else:
    #         raise Exception('Should have stopped')
    # #     # print(initial_l, initial_r)

    # assert initial_l == s[1], (s, initial_l)
    # assert initial_r == s[2], (s, initial_r)

    return s

    # i += 1
    # if r >= i:
    #     r -= i
    #     rs.append(i)
    # else:
    #     print(ls, rs)
    #     assert init_l - sum(ls) == l
    #     assert init_r - sum(rs) == r
    #     # print(sum(ls), sum(rs))
    #     return (i - 1, r, l) if swapped else (i - 1, l, r)

    # i += 1
    # if l >= i:
    #     l -= i
    #     ls.append(i)
    # else:
    #     # print(sum(ls), sum(rs))
    #     print(ls, rs)
    #     assert init_l - sum(ls) == l
    #     assert init_r - sum(rs) == r
    #     return (i-1, r, l) if swapped else (i-1, l, r)

# for x in [10, 9, 11]:
#     print('invert {}: {}'.format(x, invert_triangle(x, 0, 100)))
# raise Exception('ok')
# invert_triangle(8)
# for i in range(1, 30):
#     print(i, invert_triangle(i))
# print(invert_triangle(7))
# print(invert_triangle(8))
# print(invert_triangle(9))
# print(invert_triangle(10))
# print(invert_triangle(11))
# print(invert_triangle(12))
# print(invert_triangle(13))


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        l, r = (int(x) for x in input().split(' '))
        soln = solve_case(l, r)
        print('Case #{}: {} {} {}'.format(i, *soln), flush=True)


if __name__ == '__main__':
    run()
