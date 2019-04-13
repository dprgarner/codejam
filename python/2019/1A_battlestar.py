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


POSSIBLE = 'POSSIBLE'
IMPOSSIBLE = 'IMPOSSIBLE'


class CaseHandler(BaseInteractiveCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e03

    Practice, ~1h35, 3 incorrects
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
            ' '.join(' X' if c < 0 else (' {}'.format(c) if c < 10 else str(c)) for c in row) for row in grid
        ))
        print('\n')

    def count_one_diag(self, rows, cols, i, j):
        # assume cols >= rows
        total = -1
        if cols < rows:
            i, j = j, i
            rows, cols = cols, rows
        delta = cols - rows
        if j - i >= 0 and j - i < delta:
            total += rows
        elif j - i >= delta:
            total += rows - (j - i - delta)
        elif j - i < 0:
            total += rows - (i - j)
        else:
            raise Exception(i, j)

        return total

    def create_grid(self, rows, cols):
        # Hacky as hell but whatever.
        # Ignoring diags
        base = rows + cols - 2
        # With diags.
        grid = []
        for i in range(rows):
            grid.append([])
            for j in range(cols):
                count = base + self.count_one_diag(rows, cols, i, j)
                grid[i].append(count)
        for i in range(rows):
            for j in range(cols):
                grid[i][cols-j - 1] += self.count_one_diag(rows, cols, i, j)
        return grid

    def solve(self, rows, cols):
        # Initial values of each cell: the number of cells it shares a row,
        # col, diag with.
        grid = self.create_grid(rows, cols)
        # raise Exception(self.print_grid(grid))

        # Choose first square
        last_i, last_j = -cols - rows - 10, -1

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
                return

            entries.append((best_i, best_j))
            last_i, last_j = best_i, best_j
            grid[best_i][best_j] -= (2 * rows * cols)

            # Fix values
            for i in range(rows):
                grid[i][best_j] -= 1
            for j in range(cols):
                grid[best_i][j] -= 1
            for c in range(-rows-cols, rows + cols):
                if (
                    best_i + c >= 0 and
                    best_i + c < rows and
                    best_j + c >= 0 and
                    best_j + c < cols
                ):
                    grid[best_i + c][best_j + c] -= 1
            for c in range(-rows-cols, rows + cols):
                if (
                    best_i + c >= 0 and
                    best_i + c < rows and
                    best_j - c >= 0 and
                    best_j - c < cols
                ):
                    grid[best_i + c][best_j - c] -= 1

        return entries


CaseHandler().run()
