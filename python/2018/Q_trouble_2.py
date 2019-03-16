"""
Codejam boilerplate. Copy/paste this file with handle_case customised.
"""
from os import sys
import math


class BaseCaseHandler():
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

    def err(self, txt):
        """
        For debugging.
        """
        print(str(txt), file=sys.stderr)

    def run(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            self.handle_case(i)

    def handle_case(self, i):
        raise NotImplementedError


OK = 'OK'


class CaseHandler(BaseCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/00000000000079cb
    """

    def handle_case(self, i):
        n = int(self.read())
        integers = [int(x) for x in self.read().split(' ')]
        soln = self.solve(integers)
        self.write('Case #{}: {}'.format(i, soln))

    def solve(self, integers):
        l1 = integers[::2]
        l2 = integers[1::2]
        l1.sort()
        l2.sort()

        final_list = []
        for i, j in zip(l1, l2):
            final_list.append(i)
            final_list.append(j)
        if len(l2) < len(l1):
            final_list.append(l1[-1])

        # self.err(final_list)
        for i in range(len(final_list) - 1):
            if final_list[i] > final_list[i + 1]:
                return i

        return OK


CaseHandler().run()
