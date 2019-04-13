"""
Utility functions to copy/paste around into chess-board-like problems.
"""
from unittest import TestCase, main


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


def create_grid(rows, cols):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(count_diags(rows, cols, i, j))
    return grid


class TestGridCount(TestCase):
    def format_grid(self, grid):
        return '  ' + '\n  '.join(
            ' '.join(
                str(col)
                if col > 9
                else ' {}'.format(col)
                for col in row
            ) for row in grid
        )

    def assertGridsEqual(self, grid1, grid2):
        assert grid1 == grid2, \
            'First:\n{}\nSecond:\n{}'.format(
                self.format_grid(grid1),
                self.format_grid(grid2)
            )

    def test_square_grid(self):
        self.assertGridsEqual(create_grid(3, 3), [
            [2, 2, 2],
            [2, 4, 2],
            [2, 2, 2],
        ])
        self.assertGridsEqual(create_grid(1, 1), [[0]])
        self.assertGridsEqual(create_grid(4, 4), [
            [3, 3, 3, 3],
            [3, 5, 5, 3],
            [3, 5, 5, 3],
            [3, 3, 3, 3],
        ])
        self.assertGridsEqual(create_grid(5, 5), [
            [4, 4, 4, 4, 4],
            [4, 6, 6, 6, 4],
            [4, 6, 8, 6, 4],
            [4, 6, 6, 6, 4],
            [4, 4, 4, 4, 4],
        ])

    def test_line_grid(self):
        self.assertGridsEqual(create_grid(4, 1), [
            [0],
            [0],
            [0],
            [0],
        ])
        self.assertGridsEqual(create_grid(1, 4), [
            [0, 0, 0, 0],
        ])

    def test_long_grid(self):
        self.assertGridsEqual(create_grid(2, 5), [
            [1, 2, 2, 2, 1],
            [1, 2, 2, 2, 1],
        ])
        self.assertGridsEqual(create_grid(5, 2), [
            [1, 1],
            [2, 2],
            [2, 2],
            [2, 2],
            [1, 1],
        ])
        self.assertGridsEqual(create_grid(5, 3), [
            [2, 2, 2],
            [3, 4, 3],
            [4, 4, 4],
            [3, 4, 3],
            [2, 2, 2],
        ])


class TestGetDiags(TestCase):
    def test_square(self):
        self.assertCountEqual(get_diags(3, 3, 1, 1), [
            (0, 0),
            (2, 2),
            (0, 2),
            (2, 0),
        ])
        self.assertCountEqual(get_diags(3, 3, 0, 1), [
            (1, 0),
            (1, 2),
        ])
        self.assertCountEqual(get_diags(3, 3, 0, 0), [
            (1, 1),
            (2, 2),
        ])

    def test_rectangle_horiz(self):
        self.assertCountEqual(get_diags(3, 4, 0, 0), [
            (1, 1),
            (2, 2),
        ])
        self.assertCountEqual(get_diags(3, 4, 1, 2), [
            (0, 1),
            (2, 1),
            (0, 3),
            (2, 3),
        ])

    def test_rectangle_vert(self):
        self.assertCountEqual(get_diags(5, 3, 0, 0), [
            (1, 1),
            (2, 2),
        ])
        self.assertCountEqual(get_diags(5, 3, 1, 1), [
            (0, 0),
            (0, 2),
            (2, 0),
            (2, 2),
        ])


if __name__ == '__main__':
    main()
