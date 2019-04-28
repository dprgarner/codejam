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

    def handle_case(self, i):
        raise NotImplementedError


class CaseHandler(BaseInteractiveCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/000000000012295c
    """

    def handle_case(self, i):
        p, q = (int(x) for x in self.read().split(' '))
        people = []
        for _ in range(p):
            x_str, y_str, d = self.read().split(' ')
            people.append((int(x_str), int(y_str), d))
        x, y = self.solve(q, people)
        self.write('Case #{}: {} {}'.format(i, x, y))

    def get_n_smaller(self, sorted_arr, n):
        idx = bisect_left(sorted_arr, n)
        return idx

    def get_n_larger(self, sorted_arr, n):
        idx = bisect(sorted_arr, n)
        return len(sorted_arr) - idx

    def solve(self, grid_size, people):
        directions = {
            'N': [],
            'S': [],
            'E': [],
            'W': [],
        }
        for x, y, d in people:
            if d in ['N', 'S']:
                directions[d].append(y)
            else:
                directions[d].append(x)

        directions['N'].sort()
        directions['S'].sort()
        directions['E'].sort()
        directions['W'].sort()

        candidates_x = set([x + 1 for x in directions['E']] + [0])
        candidates_y = set([y + 1 for y in directions['N']] + [0])

        trial_x = -1
        max_val = -1
        for x in sorted(list(candidates_x)):
            value = (
                self.get_n_larger(directions['W'], x) +
                self.get_n_smaller(directions['E'], x)
            )
            if value > max_val:
                max_val = value
                trial_x = x

        trial_y = -1
        max_val = -1
        for y in sorted(list(candidates_y)):
            value = (
                self.get_n_larger(directions['S'], y) +
                self.get_n_smaller(directions['N'], y)
            )
            if value > max_val:
                max_val = value
                trial_y = y

        return trial_x, trial_y


CaseHandler().run()
