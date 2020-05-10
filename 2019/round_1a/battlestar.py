"""
Codejam boilerplate. Copy/paste this file with get_cases and handle_case
customised.
"""
from os import sys


class BaseInteractiveCaseHandler():
    """
    Boilerplate class.
    """

    def __init__(self):
        self.source = self.get_source()

    def get_source(self):
        try:
            while True:
                yield sys.stdin.readline()
        except EOFError:
            pass

    def read(self):
        return next(self.source).strip()

    def write(self, txt):
        print(str(txt))
        sys.stdout.flush()

    def run(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            self.handle_case(i)

    def handle_case(self, i):
        raise NotImplementedError


def count_diags(rows, cols, I, J):
    """
    Count all cells in the same diagonal as I and J, excluding (I, J).
    """
    total = 0
    # Count i, j s.t. i-j == I-J
    # 0 <= j = i - (I - J) < cols
    total += (
        min(rows, cols + I - J)
        - max(0, I - J)
    )

    # Count i, j s.t. i+j == I+J
    # 0 <= j = I + J - i < cols
    total += (
        min(rows, I + J + 1)
        - max(0, I + J - cols + 1)
    )
    return total - 2


def get_diags(rows, cols, I, J):
    """
    Return a list of tuples of all the entries in the same diagonal as (I, J),
    excluding (I, J).
    """

    pairs = []
    # Iterate over i, j s.t. i-j == I-J
    # 0 <= j = i - (I - J) < cols
    for i in range(
        max(0, I - J),
        min(rows, cols + I - J)
    ):
        j = i - I + J
        if i != I:
            pairs.append((i, j))

    # Iterate over i, j s.t. i+j == I+J
    # 0 <= j = I + J - i < cols
    for i in range(
        max(0, I + J - cols + 1),
        min(rows, I + J + 1)
    ):
        j = I + J - i
        if i != I:
            pairs.append((i, j))
    return pairs


POSSIBLE = 'POSSIBLE'
IMPOSSIBLE = 'IMPOSSIBLE'


class CaseHandler(BaseInteractiveCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e03

    Practice, ~1h35, 3 incorrects
    Cleaned-up with util functions and code comments
    """

    def handle_case(self, i):
        r, c = (int(x) for x in self.read().split(' '))
        soln = self.solve(r, c)
        if soln:
            soln_str = '\n'.join(
                [POSSIBLE] + [
                    '{} {}'.format(i + 1, j + 1)
                    for (i, j) in soln
                ]
            )
        else:
            soln_str = IMPOSSIBLE
        self.write('Case #{}: {}'.format(i, soln_str))

    def print_grid(self, grid):
        print('\n'.join(
            ' '.join(
                ' X'
                if c < 0
                else (
                    ' {}'.format(c)
                    if c < 10
                    else str(c)
                )
                for c in row
            )
            for row in grid
        ) + '\n')

    def create_grid(self, rows, cols):
        grid = []
        for i in range(rows):
            grid.append([])
            for j in range(cols):
                count = (rows - 1) + (cols - 1) + count_diags(rows, cols, i, j)
                grid[i].append(count)
        return grid

    def solve(self, rows, cols):
        # Greedy algorithm: assign a value to each cell, which is  the number
        # of cells it shares a row, column, or diagonal with.
        # On each iteration, check each cell and pick the cell with the most
        # available cells in the same row, column, and diagonal as that cell.

        grid = self.create_grid(rows, cols)

        # Choose the first cell to be something that no cell in the grid
        # shares a row, column, or diagonal with.
        last_i, last_j = -cols - rows - 1, -1

        entries = []
        while len(entries) < rows * cols:
            best_i, best_j = -1, -1
            best_val = -1
            for i in range(rows):
                for j in range(cols):
                    if (
                        grid[i][j] > best_val and
                        i != last_i and
                        j != last_j and
                        i + j != last_i + last_j and
                        i - j != last_i - last_j
                    ):
                        best_val = grid[i][j]
                        best_i, best_j = i, j

            if best_val < 0:
                # Ran out of avaiable cells => No solution
                return

            entries.append((best_i, best_j))
            last_i, last_j = best_i, best_j
            grid[best_i][best_j] = -1  # Should not be chosen again

            # Decrease value of cells in the same row, col, and diagonal as
            # best_i, best_j
            for i in range(rows):
                grid[i][best_j] -= 1
            for j in range(cols):
                grid[best_i][j] -= 1
            for i, j in get_diags(rows, cols, best_i, best_j):
                grid[i][j] -= 1

        return entries


CaseHandler().run()
