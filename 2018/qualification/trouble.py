"""
2018, Qualification round, B
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb
"""
from os import sys


def get_cases(source):
    cases = int(next(source))
    for i in range(1, cases + 1):
        n = int(next(source))
        numbers_str = next(source).split(' ')
        odd_numbers = []
        even_numbers = []
        for x in range(n):
            if x % 2 == 0:
                even_numbers.append(int(numbers_str[x]))
            else:
                odd_numbers.append(int(numbers_str[x]))
        yield odd_numbers, even_numbers


def handle_case(odd_numbers, even_numbers):
    odd_numbers.sort()
    even_numbers.sort()
    try:
        i = 0
        while True:
            if even_numbers[i] > odd_numbers[i]:
                return 2 * i
            if odd_numbers[i] > even_numbers[i + 1]:
                return 2 * i + 1
            i += 1
    except IndexError:
        return 'OK'


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
