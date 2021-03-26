"""
Codejam boilerplate. Copy/paste this file with get_cases and handle_case
customised.
"""
from os import sys


class BaseInteractiveCaseHandler:
    """
    Boilerplate class.
    """

    def __init__(self):
        self.source = self.get_source()
        self.debug_mode = True
        # self.debug_mode = False

    def get_source(self):
        try:
            while True:
                yield sys.stdin.readline()
        except EOFError:
            pass

    def read(self):
        input_ = next(self.source).strip()
        self.debug("In: {}".format(input_))
        return input_

    def write(self, *txt):
        self.debug("Out:", *txt)
        print(*txt)
        sys.stdout.flush()

    def debug(self, *txt):
        if not self.debug_mode:
            return
        print(*txt, file=sys.stderr)
        sys.stderr.flush()

    def run(self):
        # Example read
        cases, self.a, self.b = (int(x) for x in self.read().split(" "))
        if self.a < 10**9 - 50:
            raise Exception('no idea')
        for i in range(1, cases + 1):
            self.debug("Case", i)
            self.handle_case(i)

    def handle_case(self, *args):
        raise NotImplementedError


class WrongAnswerException(Exception):
    pass


class FoundException(Exception):
    pass


class CaseHandler(BaseInteractiveCaseHandler):
    def throw_dart(self, x, y):
        self.write("{} {}".format(x, y))
        result = self.read()
        if input_ == "WRONG":
            raise WrongAnswerException
        if result == "CENTER":
            raise FoundException
        return result == "HIT"

    def refine(self):
        for i in range()
        x, y = 0, 0
        result = self.throw_dart(x, y)

    def handle_case(self, _i):
        try:
            while True:
                self.refine()
        except FoundException:
            pass


CaseHandler().run()
