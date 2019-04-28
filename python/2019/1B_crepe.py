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
            directions[d].append((x, y))

        directions['N'].sort(key=lambda xy: xy[1])
        directions['S'].sort(key=lambda xy: xy[1])
        directions['E'].sort(key=lambda xy: xy[0])
        directions['W'].sort(key=lambda xy: xy[0])

        candidates_y = set([
            y+1 for _, y in directions['N']
        ] + [
            y-1 for _, y in directions['S']
        ] + [0])
        candidates_x = set([
            x+1 for x, _ in directions['E']
        ] + [
            x-1 for x, _ in directions['W']
        ] + [0])

        # No reason to recreate the array on every trial.
        dir_1d = {}
        dir_1d['N'] = [y for _, y in directions['N']]
        dir_1d['S'] = [y for _, y in directions['S']]
        dir_1d['E'] = [x for x, _ in directions['E']]
        dir_1d['W'] = [x for x, _ in directions['W']]

        max_val = -1
        trial = -1, -1
        # Max. trial cases: 250,000. Looks like it was fast enough.
        for x in sorted(list(candidates_x)):
            for y in sorted(list(candidates_y)):
                value = 0
                value += self.get_n_larger(dir_1d['S'], y)
                value += self.get_n_smaller(dir_1d['N'], y)
                value += self.get_n_larger(dir_1d['W'], x)
                value += self.get_n_smaller(dir_1d['E'], x)

                if value > max_val:
                    max_val = value
                    trial = x, y

        return trial


CaseHandler().run()
