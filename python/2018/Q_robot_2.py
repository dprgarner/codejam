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


IMPOSSIBLE = 'IMPOSSIBLE'


class CaseHandler(BaseCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/0000000000007966
    """

    def handle_case(self, i):
        d_str, p = self.read().split(' ')
        d = int(d_str)
        soln = self.solve(d, p)
        self.write('Case #{}: {}'.format(i, soln))

    def solve(self, d, p):
        # Always replace CS with SC
        # Latest CS always the most valuable to swap

        # Count S's. Min damage is total # of S's.
        min_ = sum(1 if c == 'S' else 0 for c in p)
        if min_ > d:
            return IMPOSSIBLE

        # Get damage.
        damage = 0
        charge = 1
        for c in p:
            if c == 'C':
                charge *= 2
            if c == 'S':
                damage += charge

        if damage <= d:
            return 0

        # Find latest "CS" and swap
        for i in range(len(p) - 1, 0, -1):
            if p[i] == 'S' and p[i - 1] == 'C':
                new_str = p[:i-1] + 'SC' + p[i+1:]
                # self.err(new_str)
                return 1 + self.solve(d, new_str)

        raise Exception('???')


CaseHandler().run()
