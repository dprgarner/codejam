"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209aa0
Got nowhere with this one. :(

Plan for solution:
Partition k into n numbers in the range 1 to n, where the n numbers in the partition can take 1 or 3 possible values.
E.g. if k = n*n, partitioned into 1 "block" of n * n.
if k = n*n - 2, partition into 2 "blocks" of (n - 1) * n and 1 * (n - 2).

If 1 possible value: just put the same number on the trace.
If 3 possible values: rotate around a simple solution.

Is it always possible to partition k into 1 or 3 possible values?
Not if k = n*n - 1.
If k = n*n - 1, there's no solution. All but one of the diag elements is "n" and the last one is "n-1", so you'll always have a column of n-1 numbers that can only take n-2 possible values. (It's also impossible to partition into 1 or 3 poss. values.)

Intuition is that there's a solution iff the partition into 1 or 3 values exists, but I've no idea how to prove this.
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


def solve_case(n, k):
    matrix = [
        [1, 3, 2],
        [3, 2, 1],
        [2, 1, 3],
    ]
    assert vestigium(matrix) == (k, 0, 0), vestigium(matrix)
    return matrix


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
        else:
            print("Case #{}: IMPOSSIBLE".format(i), flush=True)


if __name__ == "__main__":
    run()
