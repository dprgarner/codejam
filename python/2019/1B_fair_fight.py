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


class CaseHandler(BaseInteractiveCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122838
    Quick solution. Doesn't even attempt to solve the large n case.
    """

    def handle_case(self, i):
        n, k = (int(x) for x in self.read().split(' '))
        c_i = [int(x) for x in self.read().split(' ')]
        d_i = [int(x) for x in self.read().split(' ')]

        soln = self.solve(c_i, d_i, k)
        self.write('Case #{}: {}'.format(i, soln))

    def solve(self, c_i, d_i, k):
        ff = 0
        n = len(c_i)
        for l in range(n):
            for r in range(l, n):
                if abs(max(c_i[l:r + 1]) - max(d_i[l:r + 1])) <= k:
                    ff += 1
        return ff


CaseHandler().run()
