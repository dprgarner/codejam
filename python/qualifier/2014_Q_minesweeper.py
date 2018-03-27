from math import ceil
from codejam import CodeJamParser


# 20:45
# Gave up at 22:30

# Spent another ~2 hours debugging every single damn case I could think of
# before I realised that I needed to print the word "Impossible" on the next
# line. Fucking. Hell.

IMPOSSIBLE = '\nImpossible'


def check_board(grid):
    zeroes = [
        [c for c in row]
        for row in grid
    ]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if not col:
                # It's not a mine; label itself and all neighbours true
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if (
                            y + i >= 0 and
                            y + i < len(grid) and
                            x + j >= 0 and
                            x + j < len(row)
                        ):
                            zeroes[y + i][x + j] = False

    one_away_from_zero = [
        [c for c in row]
        for row in zeroes
    ]
    for i, row in enumerate(zeroes):
        for j, col in enumerate(row):
            if col:
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        # print(x, y)
                        if (
                            y + i >= 0 and
                            y + i < len(zeroes) and
                            x + j >= 0 and
                            x + j < len(row)
                        ):
                            one_away_from_zero[y + i][x + j] = True

    mines_or_one_away_from_zero = [
        [c for c in row]
        for row in one_away_from_zero
    ]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if not col:
                mines_or_one_away_from_zero[i][j] = True
    mines_or_one_away_from_zero[0][0] = True
    return all(all(row) for row in mines_or_one_away_from_zero)


def draw_board(rows, cols, spaces):
    # True - space
    # False - mine
    grid = [[
        False for _ in range(cols)
    ] for _ in range(rows)]

    for (i, j) in spaces:
        grid[i][j] = True

    board_str = '\n'.join([
        ''.join([
            '.' if c else '*'
            for c in row
        ])
        for row in grid 
    ])

    return '\nc' + board_str[1:]


class Run(CodeJamParser):
    """
    2014, Qualification round, C
    https://code.google.com/codejam/contest/2974486/dashboard#s=p0
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            r, c, m = [
                int(n) for n in next(self.source).split(' ')
            ]
            yield r, c, m

    def handle_case(self, rows, cols, mines):
        spaces = rows * cols - mines

        if spaces == 1:
            return draw_board(rows, cols, [(0, 0)])

        # These must be handled first
        if rows == 1:
            return draw_board(1, cols, [(0, j) for j in range(spaces)])
        if cols == 1:
            return draw_board(rows, 1, [(i, 0) for i in range(spaces)])

        if spaces == 2 and rows * cols > 2:
            return IMPOSSIBLE

        if spaces % 2 == 1 and (rows == 2 or cols == 2):
            return IMPOSSIBLE

        if rows == 2:
            return draw_board(2, cols, [
                (0, j) for j in range(spaces // 2)
            ] + [
                (1, j) for j in range(spaces // 2)
            ])
        if cols == 2:
            return draw_board(rows, 2, [
                (i, 0) for i in range(spaces // 2)
            ] + [
                (i, 1) for i in range(spaces // 2)
            ])

        if spaces % 2 == 1 and spaces < 9:
            return IMPOSSIBLE

        # Always a solution in all other cases.
        # Trace along from the top left.
        if spaces < 2 * cols and spaces % 2 == 0:
            return draw_board(rows, cols, (
                [(0, j) for j in range(spaces // 2)]
                + [(1, j) for j in range(spaces // 2)]
            ))
        if spaces < 2 * cols and spaces % 2 == 1:
            last_col_with_space = (spaces - 3) // 2
            return draw_board(rows, cols, (
                [(0, j) for j in range(last_col_with_space)]
                + [(1, j) for j in range(last_col_with_space)]
                + [(2, 0), (2, 1), (2, 2)]
            ))
        if spaces == 2 * cols + 1:
            return draw_board(rows, cols, (
                [(i, j) for i in range(2) for j in range(cols - 1)]
                + [(2, 0), (2, 1), (2, 2)]
            ))
        if (spaces % cols) == 1:
            filled_rows = spaces // cols
            return draw_board(rows, cols, ([
                (i, j)
                for i in range(filled_rows)
                for j in range(cols)
                if i != filled_rows - 1 or j != cols - 1
            ] + [(filled_rows, 0), (filled_rows, 1)]))

        filled_rows = spaces // cols
        return draw_board(rows, cols, ([
            (i, j)
            for i in range(filled_rows)
            for j in range(cols)
        ] + [
            (filled_rows, j)
            for j in range(spaces % cols)
        ]))



if __name__ == '__main__':
    Run()
