from os import sys
from random import choice


class GopherException(Exception):
    pass


class GopherComplete(Exception):
    pass


class Gopher(object):
    """
    Slightly different this time.
    2018, Qualification round, C
    https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/0000000000007a30
    """

    @staticmethod
    def get_lines_from_stdin():
        try:
            while True:
                yield sys.stdin.readline()
        except EOFError:
            pass

    def __init__(self):
        self.source = self.get_lines_from_stdin()
        self.dest = sys.stdout

        cases = int(next(self.source))
        for i in range(1, cases + 1):
            area = int(next(self.source))
            try:
                self.handle_case(area)
            except GopherComplete:
                self.debug('Done in {} attempts'.format(self.attempts))


    def read_pair(self):
        i, j = (int(x) for x in next(self.source).split(' '))
        if i == -1 or j == -1:
            raise GopherException('Test failed')
        if i == 0:
            raise GopherComplete('Done')
        return i, j

    def write_pair(self, i, j):
        print('{} {}'.format(i, j), flush=True)

    def count_values(self, numbers):
        values = []
        for _ in range(len(numbers)):
            values.append([-1] * len(numbers[0]))

        for i in range(1, len(numbers) - 1):
            for j in range(1, len(numbers[0]) - 1):
                # Add up False neighbours of (i, j)
                total = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if not numbers[i+x][j+y]:
                            total += 1
                values[i][j] = total
        return values

    def print_values(self, values):
        return '\n' + '\n'.join(
            ' '.join(
                '.'
                if n == -1
                else '{}'.format(n)
                for n in row
            )
            for row in values
        )

    def bounds(self, numbers):
        rows_with_numbers = [any(row) for row in numbers]
        top_i = rows_with_numbers.index(True)
        bottom_i = len(rows_with_numbers) - rows_with_numbers[::-1].index(True) - 1

        cols_with_numbers = [False] * len(numbers[0])
        for i in range(len(numbers)):
            for j in range(len(numbers[0])):
                if numbers[i][j]:
                    cols_with_numbers[j] = True
        left_j = cols_with_numbers.index(True)
        right_j = len(cols_with_numbers) - cols_with_numbers[::-1].index(True) - 1

        return (top_i, left_j), (bottom_i, right_j)

    def debug(self, msg):
        pass
        # print(msg, file=sys.stderr, flush=True)

    def handle_case(self, area):
        # Draw in top-left area. No point accounting for the whole 1000^2 grid.
        play_area = 100

        # Just pick an area around the centre.
        numbers = []
        for _ in range(play_area):
            numbers.append([False] * play_area)

        choice_i = play_area // 2
        choice_j = play_area // 2
        self.attempts = 0

        while True:
            self.attempts += 1
            self.write_pair(choice_i, choice_j)
            i, j = self.read_pair()
            numbers[i][j] = True

            # Get bounds of current dug area
            (top, left), (bottom, right) = self.bounds(numbers)
            # Use these to get the range of useful squares to play in
            if (1 + bottom - top) * (1 + right - left) < area:
                top -= 1
                left -= 1
                bottom += 2
                right += 2

            values = self.count_values([
                row[left:right+1]
                for row in numbers[top:bottom+1]
            ])

            best = max(col for row in values for col in row)
            matches = list(filter(None, [
                (top + i, left + j)
                if values[i][j] == best
                else None
                for i in range(len(values))
                for j in range(len(values[0]))
            ]))
            if best == 0:
                raise GopherException('Something went wrong.')

            choice_i, choice_j = choice(matches)


Gopher()
