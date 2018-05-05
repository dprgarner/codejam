"""
1B, A, 2018
https://codejam.withgoogle.com/2018/challenges/0000000000007764/dashboard
"""
from os import sys
import math


def get_cases(source):
    cases = int(next(source))
    for i in range(1, cases + 1):
        n, l = (int(x) for x in next(source).split(' '))
        cs = [int(x) for x in next(source).split(' ')]
        yield n, cs


def better_round(n):
    if n % 1 == 0.5:
        return int(n) + 1
    return round(n)


def handle_case(n, cs):
    if 100 / n % 1 == 0:
        # No useful adding.
        return 100

    current_percent = 0
    people_left = n - sum(cs)

    target_cs = []
    for c in cs + [0]:
        current_percent += better_round(100 * c / n)
        current_better_rounding = 100 * (c / n) % 1

        if current_better_rounding < 0.5:
            # How many people to make this useful?
            if 100 / n < 0.5:
                # Each person is less than 0.5%
                x = math.ceil(n * (0.5 + int(100 * c / n) - 100 * c / n) / 100)
                target_cs.append((c, 1, x))
            else:
                # Add until it goes over.
                x = 0
                while 100 * ((c + x) / n) % 1 < 0.5:
                    x += 1
                # How much would the percent go up by choosing this one?
                print(c, x, 100 * (c + x) / n)
                value = better_round(100 * (c + x) / n) - better_round(100 * c / n)
                target_cs.append((c, value, x))
        print('cp', current_percent)

    blank_c = target_cs.pop()
    target_cs.sort(key=lambda x: x[2])
    print(target_cs, blank_c)

    # Always pic existing language first before starting a new one.
    while people_left > 0 and target_cs:
        c, value, x = target_cs.pop(0)
        print('pick c', c)
        if x > people_left:
            current_percent += (better_round(100 * (c + people_left) / n) - better_round(100 * c / n))
            people_left = 0
            break
        people_left -= x
        current_percent += value
        print('cp', current_percent)

    if people_left:
        # Just create new languages.
        c, value, x = blank_c
        new_langs = math.floor(people_left / x)
        current_percent += value * new_langs
        people_left -= (x * new_langs)

    if people_left:
        # One last language (which won't be better_rounded up).
        current_percent += better_round(100 * (c + people_left) / n)

    return current_percent


"""
Boilerplate functions.
"""
def get_source():
    try:
        while True:
            yield sys.stdin.readline()
    except EOFError:
        pass


def run(get_cases, handle_case):
    source = get_source()
    dest = sys.stdout
    for i, case in enumerate(get_cases(source)):
        result = handle_case(*case)
        dest.write('Case #{}: {}\n'.format(i + 1, result))


run(get_cases, handle_case)
