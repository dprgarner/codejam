"""
Codejam boilerplate. Copy/paste this file with get_cases and handle_case
customised.
"""
from os import sys
from bisect import bisect, bisect_left


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
        # self.nimber_cache.debug()

    def handle_case(self, i):
        raise NotImplementedError


RADIOACTIVE = '#'
EMPTY = '.'


class NimberCache():
    _cache = {}

    def get(self, grid):
        if not grid:
            return 0
        return self._cache.get(self.to_str(grid))

    def to_str(self, grid):
        return '\n'.join(grid)

    def all_str_versions(self, grid):
        yield self.to_str(grid)
        yield self.to_str(grid[::-1])
        yield self.to_str([
            row[::-1] for row in grid
        ])
        yield self.to_str([
            row[::-1] for row in grid[::-1]
        ])

        rotated_grid = [
            ''.join([row[j] for row in grid])
            for j in range(len(grid[0]))
        ]
        yield self.to_str(rotated_grid)
        yield self.to_str(rotated_grid[::-1])
        yield self.to_str([
            row[::-1] for row in rotated_grid
        ])
        yield self.to_str([
            row[::-1] for row in rotated_grid[::-1]
        ])

    def set(self, grid, value):
        for k in self.all_str_versions(grid):
            self._cache[k] = value

    def debug(self):
        for c, value in self._cache.items():
            print(c, 'has nimber', value)


class CaseHandler(BaseInteractiveCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134cdf

    Post-contest attempt.
    """

    def __init__(self):
        super().__init__()
        self.nimber_cache = NimberCache()
        self.prepopulate_cache()

    def prepopulate_cache(self):
        for i in range(1, 17):
            for j in range(i, 17):
                grid = []
                for _ in range(i):
                    grid.append('.' * j)
                # Sets in the cache
                self.get_nimber(grid)

    def handle_case(self, i):
        r, c = (int(x) for x in self.read().split(' '))
        rows = []
        for _ in range(r):
            rows.append(self.read())
        soln = self.solve(rows)
        self.write('Case #{}: {}'.format(i, soln))

    def get_valid_moves(self, rows):
        valid_row_moves = []
        for i, row in enumerate(rows):
            invalid_row = False
            open_spaces = 0
            for c in row:
                if c == RADIOACTIVE:
                    invalid_row = True
                    break
                else:
                    open_spaces += 1
            # row invalid
            if not invalid_row:
                valid_row_moves.append(('H', i, open_spaces))

        valid_col_moves = []
        for j in range(len(rows[0])):
            invalid_col = False
            open_spaces = 0
            for row in rows:
                if row[j] == RADIOACTIVE:
                    invalid_col = True
                    break
                else:
                    open_spaces += 1
            if not invalid_col:
                valid_col_moves.append(('V', j, open_spaces))

        return valid_row_moves + valid_col_moves

    def split(self, rows, move):
        direction, idx, _ = move
        if direction == 'H':
            return [s for s in (rows[:idx], rows[idx + 1:]) if s]

        return [s for s in (
            [row[:idx] for row in rows],
            [row[idx + 1:] for row in rows]
        ) if s[0]]

    def mex(self, values):
        sorted_values = sorted(values)
        count = 0

        while sorted_values:
            if sorted_values[0] > count:
                return count
            while sorted_values and sorted_values[0] <= count:
                sorted_values.pop(0)
            count += 1

        return count

    def nim_sum(self, numbers):
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        if len(numbers) > 2:
            # Shouldn't happen?
            return self.nim_sum([numbers[0], self.nim_sum(numbers[1:])])

        a_str, b_str = bin(numbers[0])[2:], bin(numbers[1])[2:]
        if numbers[0] < numbers[1]:
            a_str, b_str = b_str, a_str

        b_str = '0' * (len(a_str) - len(b_str)) + b_str

        return int(''.join(
            '0' if a_str[i] == b_str[i] else '1'
            for i in range(len(a_str))
        ), 2)

    def get_nimber(self, rows):
        value = self.nimber_cache.get(rows)
        if value != None:
            return value

        # Calculate it
        possible_move_nimbers = []
        for move in self.get_valid_moves(rows):
            subgrid_nimbers = [
                self.get_nimber(subgrid)
                for subgrid in self.split(rows, move)
            ]
            possible_move_nimbers.append(self.nim_sum(subgrid_nimbers))
        value = self.mex(possible_move_nimbers)

        self.nimber_cache.set(rows, value)
        return value

    def solve(self, rows):
        possible_moves = 0
        for move in self.get_valid_moves(rows):
            _, _, count = move
            subgrid_nimbers = [
                self.get_nimber(subgrid)
                for subgrid in self.split(rows, move)
            ]
            move_value = self.nim_sum(subgrid_nimbers)
            if move_value == 0:
                possible_moves += count
        return possible_moves


CaseHandler().run()
