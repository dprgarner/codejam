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
        if input_ == "N":
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
        cases = (int(x) for x in self.read().split(" "))
        for i in range(1, cases + 1):
            self.debug("")
            self.handle_case(i)

    def handle_case(self, i):
        raise NotImplementedError


class CaseHandler(BaseInteractiveCaseHandler):
    def handle_case(self, _i):
        pass


CaseHandler().run()
