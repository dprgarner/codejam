"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209aa0
Didn't get a working solution for this one. :(
"""


def has_repeated_entry(l):
    entries = set(l)
    for n in l:
        if n in entries:
            entries.remove(n)
        else:
            return True
    return False


def vestigium(matrix):
    repeated_rows = 0
    for row in matrix:
        if has_repeated_entry(row):
            repeated_rows += 1

    repeated_cols = 0
    for j in range(len(matrix[0])):
        if has_repeated_entry([matrix[i][j] for i in range(len(matrix))]):
            repeated_cols += 1

    tr = 0
    for i in range(len(matrix)):
        tr += matrix[i][i]
    return tr, repeated_rows, repeated_cols


def find_triple(n, k):
    """
    Given n and k, find a,b,c s.t. a(n-2) + b + c == k, where a != b != c and
    all are in 1 to n.
    """
    assert n <= k, "n too big"
    assert n * n >= k, "n too small"
    assert k % n != 0, "should not be looking for diff abc"
    assert k not in {n * n - 1, n + 1}, "no soln"
    a = k // (n - 2)
    rem = k % a
    print(a, rem)
    raise Exception("TODO")


template_matrices = {}


def build_cycle_matrix(n):
    return [[(i % n) + 1 for i in range(s, n + s)] for s in range(n, 0, -1)]


def map_matrix(matrix, permutation):
    print(permutation)
    if all(k == v for k, v in permutation.items()):
        return matrix
    return [[permutation.get(col, col) for col in row] for row in matrix]


def multiply_transpositions(*trans):
    permuted = set()
    permutation = {}
    for i, j in trans:
        permuted.update((i, j))
    for origin in permuted:
        destination = origin
        for i, j in trans:
            if i == destination:
                destination = j
            elif j == destination:
                destination = i
        permutation[origin] = destination
    return permutation


def solve_case(n, k):
    if k in {n * n - 1, n + 1}:
        return None

    if n not in template_matrices:
        template_matrices[n] = build_cycle_matrix(n)
    matrix = [row for row in template_matrices[n]]

    if k % n == 0:
        a = k // n
        return map_matrix(matrix, {1: a, a: 1})

    a, b, c = find_triple(n, k)
    matrix.insert(len(matrix) - 2, matrix.pop())
    permutation = multiply_transpositions((1, a), (2, b), (n, c))
    return map_matrix(matrix, permutation)


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n, k = (int(x) for x in input().split(" "))
        soln = solve_case(n, k)
        if soln:
            print(
                "Case #{}: POSSIBLE\n{}".format(
                    i, "\n".join(" ".join(str(col) for col in row) for row in soln)
                ),
                flush=True,
            )
            assert vestigium(soln) == (k, 0, 0), vestigium(soln)
        else:
            print("Case #{}: IMPOSSIBLE".format(i), flush=True)


if __name__ == "__main__":
    run()
