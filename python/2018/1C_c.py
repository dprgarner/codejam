"""
Codejam boilerplate. Copy/paste this file with get_cases and handle_case
customised.
"""
from os import sys


def get_cases(source):
    cases = int(next(source))
    for i in range(1, cases + 1):
        n = int(next(source))
        weights = [int(w) for w in next(source).split(' ')]
        yield n, weights


def get_desc_seq(ants, truncate):
    max_ants = 0
    for i, ant in enumerate(ants[:truncate]):
        if max_ants <= ant:
            max_ants = ant
            pos = i

    if max_ants == 1:
        return False

    found = False
    if ants[:pos]:
        for ant in ants[:pos]:
            if ant >= max_ants - 1:
                found = True
                break
    if not found:
        ants[pos] = ants[pos] - 1
        return True
    return get_desc_seq(ants, pos)


def handle_case(n, weights):
    sorted_by_weight = sorted(enumerate(weights), key=lambda x: x[1])

    max_ants = []
    # Start by weight only.
    for i, w in enumerate(weights):
        weight_limit = 6 * w
        total_ants = 0
        total_weight = 0
        for j, w2 in sorted_by_weight:
            if j < i:
                total_ants += 1
                total_weight += w2
            if total_weight > weight_limit:
                total_ants -= 1
                break
        max_ants.append(total_ants + 1)

    # Iterate through. Look for a sequence 1, 2, ... N for largest N. If
    # for a given k there is no k-1, replace k with k-1.
    while get_desc_seq(max_ants, n):
        pass

    return max(max_ants)


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
