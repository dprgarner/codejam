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


RADIOACTIVE = True
EMPTY = False


class CaseHandler(BaseInteractiveCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134cdf

    Didn't get anywhere with this one.
    """

    def handle_case(self, i):
        r, c = (int(x) for x in self.read().split(' '))
        rows = []
        for _ in range(r):
            row = [
                EMPTY if c == '.' else RADIOACTIVE
                for c in self.read()
            ]
            rows.append(row)
        soln = self.solve(rows)
        self.write('Case #{}: {}'.format(i, soln))

    def is_dead(self, rows):
        # Radio in all rows?
        has_radio_in_rows = []
        for row in rows:
            has_radio = False
            for c in row:
                if c == RADIOACTIVE:
                    has_radio = True
            has_radio_in_rows.append(has_radio)

        # Radio in all cols?
        has_radio_in_cols = []
        for j in range(len(rows[0])):
            has_radio = False
            for row in rows:
                if row[j] == RADIOACTIVE:
                    has_radio = True
            has_radio_in_cols.append(has_radio)

        return all(has_radio_in_rows) and all(has_radio_in_cols)

    def solve(self, rows):
        return self.is_dead(rows)


CaseHandler().run()
