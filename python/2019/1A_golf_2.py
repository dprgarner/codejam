"""
Codejam boilerplate. Copy/paste this file with get_cases and handle_case
customised.
"""
from os import sys
import math


class WrongAnswerException(Exception):
    pass


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
        if input_ == "-1":
            raise WrongAnswerException
        return input_

    def write(self, txt):
        print(txt)
        self.debug("Out: {}".format(txt))
        sys.stdout.flush()

    def debug(self, txt):
        if not self.debug_mode:
            return
        print(txt, file=sys.stderr)
        sys.stderr.flush()

    def run(self):
        cases, self.n, self.m = (int(x) for x in self.read().split(" "))
        for i in range(1, cases + 1):
            self.debug("")
            self.handle_case(i)

    def handle_case(self, i):
        raise NotImplementedError


COPRIMES = [3, 4, 5, 7, 11, 13, 17]
PROD = 1
for x in COPRIMES:
    PROD *= x


RECIPROCALS = [PROD // x for x in COPRIMES]
# Numbers which are inverses of the reciprocals mod the coprimes
MODS = [2, 3, 4, 1, 6, 2, 16]
COEFFS = [x * y for (x, y) in zip(RECIPROCALS, MODS)]

assert [a % b for (a, b) in zip(COEFFS, COPRIMES)] == [1, 1, 1, 1, 1, 1, 1]


class CaseHandler(BaseInteractiveCaseHandler):
    def query(self, request_ints):
        self.write(" ".join(str(int_) for int_ in request_ints))
        response_ints = [int(x) for x in self.read().split(" ")]
        return response_ints

    def guess(self, int_):
        self.write(int_)
        assert self.read() == "1"

    def handle_case(self, _i):
        mods = [sum(self.query([i] * 18)) for i in COPRIMES]
        self.debug(mods)
        x = sum(a * COEFFS[i] for i, a in enumerate(mods)) % PROD
        self.guess(x)


CaseHandler().run()
