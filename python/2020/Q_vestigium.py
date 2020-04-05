"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c
"""


def has_repeated_entry(l):
    entries = set(l)
    for n in l:
        if n in entries:
            entries.remove(n)
        else:
            return True
    return False


def solve_case(matrix):
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


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n_rows = int(input())
        rows = []
        for _ in range(n_rows):
            cols = list(int(x) for x in input().split(" "))
            rows.append(cols)
        soln = solve_case(rows)
        print("Case #{}: {} {} {}".format(i, *soln), flush=True)


if __name__ == "__main__":
    run()
