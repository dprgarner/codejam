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
    https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231
    """

    def handle_case(self, i):
        a, b = self.solve(self.read())
        self.write('Case #{}: {} {}'.format(i, a, b))

    def solve(self, n_str):
        # Create new string with 0s for each non-4, 1's for each 4
        list_a = []
        list_b = []
        for digit in n_str:
            if digit == '4':
                list_a.append(str(3))
                list_b.append(str(1))
            else:
                list_a.append(digit)
                list_b.append(str(0))

        while list_b and list_b[0] == '0':
            list_b.pop(0)
        str_a = ''.join(list_a)
        str_b = ''.join(list_b or ['0'])

        return str_a, str_b


CaseHandler().run()
