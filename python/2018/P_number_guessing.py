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


CORRECT = 'CORRECT'
TOO_SMALL = 'TOO_SMALL'
TOO_BIG = 'TOO_BIG'


class CaseHandler(BaseInteractiveCaseHandler):
    def handle_case(self, _):
        a, b = (int(x) for x in self.read().split(' '))
        n = int(self.read())

        while True:
            next_guess = (a + 1 + b) // 2
            self.write(next_guess)
            result = self.read()
            if result == CORRECT:
                return
            if result == TOO_SMALL:
                a = next_guess
            if result == TOO_BIG:
                b = next_guess - 1


CaseHandler().run()
