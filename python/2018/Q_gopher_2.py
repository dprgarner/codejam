"""
Codejam boilerplate. Copy/paste this file with get_cases and handle_case
customised.
"""
from os import sys
import math


class GopherComplete(Exception):
    pass


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


class CaseHandler(BaseInteractiveCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/0000000000007a30
    """

    def get_coords(self):
        i, j = (int(x) for x in self.read().split(' '))
        if i == 0 and j == 0:
            raise GopherComplete()
        if i == -1 and j == -1:
            raise Exception('Something went wrong.')
        return i - 100, j - 100

    def put_coords(self, i, j):
        self.write('{} {}'.format(100 + i, 100 + j))

    def get_plot_dims(self, area):
        if area <= 9:
            return 3, 3
        width = int(math.sqrt(area))
        height = (
            area // width
            if area / width == area // width
            else 1 + area // width
        )
        return width, height

    def raise_plots(self, plots):
        """
        For debugging.
        """
        raise Exception('\n' + '\n'.join(
            ' '.join(
                'X' if col == True else (str(col) if col else '.') for col in row)
            for row in plots
        ))

    def find_max(self, plot_values):
        max_value = max(max(row) for row in plot_values)
        for i in range(len(plot_values)):
            for j in range(len(plot_values[0])):
                if plot_values[i][j] == max_value:
                    return i, j

    def handle_case(self, _):
        area = int(self.read())
        width, height = self.get_plot_dims(area)

        # Plots that have been filled.
        plot_filled = []
        for _ in range(height):
            plot_filled.append([False] * width)

        # The number of unfilled plots next to a square (that aren't at the
        # edge.)
        plot_values = []
        for _ in range(height):
            plot_values.append([0] * width)

        for i in range(1, height - 1):
            for j in range(1, width - 1):
                plot_values[i][j] = 9

        while True:
            # Pick the point with the highest chance of filling a vacant plot
            # each time.
            self.put_coords(*self.find_max(plot_values))
            try:
                new_i, new_j = self.get_coords()
            except GopherComplete:
                return

            if not plot_filled[new_i][new_j]:
                # Neighbours now have 1 less value
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        if (
                            new_i + i > 0 and new_i + i < height - 1 and
                            new_j + j > 0 and new_j + j < width - 1
                        ):
                            plot_values[new_i + i][new_j + j] = max(
                                0, plot_values[new_i + i][new_j + j] - 1
                            )
            plot_filled[new_i][new_j] = True
            # self.raise_plots(plot_values)
            # self.raise_plots(plot_filled)


CaseHandler().run()
