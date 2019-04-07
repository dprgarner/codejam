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
    https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da
    """

    def handle_case(self, i):
        n = int(self.read())
        moves_str = self.read()
        soln = self.solve(n, moves_str)
        self.write('Case #{}: {}'.format(i, soln))

    def solve(self, n, moves):
        soln_chars = []
        for char in moves:
            soln_chars.append('E' if char == 'S' else 'S')
        return ''.join(soln_chars)


CaseHandler().run()
