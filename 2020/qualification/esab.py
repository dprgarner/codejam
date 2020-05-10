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
        # self.debug_mode = True
        self.debug_mode = False

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
        cases, self.b = (int(x) for x in self.read().split(" "))
        for i in range(1, cases + 1):
            self.debug("")
            self.handle_case(i)

    def handle_case(self, i):
        raise NotImplementedError


class CaseHandler(BaseInteractiveCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9e
    """

    def query(self, idx):
        self.write(idx + 1)
        self.queries += 1
        return int(self.read())

    def guess(self, bits):
        answer = "".join(str(b) for b in bits)
        self.write(answer)
        assert self.read() == "Y"

    def handle_case(self, _i):
        palindrome_digit = None
        invert_digit = None
        self.queries = 0

        bits = [None] * self.b
        idx = 0
        while idx < self.b / 2:
            if self.queries % 10 == 0:
                # Get the anti/palindrome digits
                self.debug(
                    "querying invert digit"
                    if invert_digit is not None
                    else "No invert digit"
                )
                inv_query = self.query(invert_digit or 0)
                inv_changed = (
                    invert_digit is not None and bits[invert_digit] != inv_query
                )
                if inv_changed:
                    bits = [None if b is None else (1 - b) for b in bits]
                    self.debug("inverting")

                self.debug(
                    "querying palindrome_digit"
                    if palindrome_digit is not None
                    else "No palindrome_digit"
                )
                p_query = self.query(palindrome_digit or 0)
                p_changed = (
                    palindrome_digit is not None and bits[palindrome_digit] != p_query
                )
                if p_changed:
                    bits = list(reversed(bits))
                    self.debug("reversing")
                self.debug("---")
            else:
                bits[idx] = self.query(idx)
                bits[self.b - idx - 1] = self.query(self.b - idx - 1)
                if bits[idx] == bits[self.b - idx - 1]:
                    invert_digit = idx
                else:
                    palindrome_digit = idx
                idx += 1

        self.guess(bits)


CaseHandler().run()
