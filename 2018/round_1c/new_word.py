"""
1C, question A, 2018.
"""
from os import sys


IMPOSSIBLE = '-'


def get_cases(source):
    cases = int(next(source))
    for i in range(1, cases + 1):
        n, l = [int(s) for s in next(source).split(' ')]
        words = []
        for _ in range(n):
            words.append(next(source).strip())
        yield l, words


def get_prod_of_set_lengths(sets):
    prod = 1
    for s in sets:
        prod *= len(s)
    return prod


def handle_case(l, words):
    chars_at_position = [set() for _ in range(l)]
    for word in words:
        for i, char in enumerate(word):
            chars_at_position[i].add(char)

    if len(words) == get_prod_of_set_lengths(chars_at_position):
        # Every possible combination formed
        return IMPOSSIBLE

    # Which stubs have potential?
    stub = ''
    for level in range(l):
        current_level_stub = stub
        for c in chars_at_position[level]:
            potential_stub = current_level_stub + c
            words_starting_with_stub = len(
                [w for w in words if w.startswith(potential_stub)]
            )
            if words_starting_with_stub != get_prod_of_set_lengths(
                chars_at_position[level + 1:]
            ):
                # Stub's a good 'un.
                break
        stub = potential_stub

    return stub


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
