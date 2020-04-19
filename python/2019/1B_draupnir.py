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
        if input_ == "-1":
            raise WrongAnswerException
        return input_

    def write(self, txt):
        print(txt)
        self.debug("Out: {}".format(txt))
        sys.stdout.flush()

    def debug(self, *txt):
        if not self.debug_mode:
            return
        print(*txt, file=sys.stderr)
        sys.stderr.flush()

    def run(self):
        cases, self.w = (int(x) for x in self.read().split(" "))
        for i in range(1, cases + 1):
            self.debug("")
            self.handle_case(i)


class CaseHandler(BaseInteractiveCaseHandler):
    def query(self, day):
        self.write(day)
        n = int(self.read())
        binary = "{0:b}".format(n)
        while len(binary) < 63:
            binary = "0" + binary
        return binary

    def guess(self, ints):
        self.write(" ".join(str(x) for x in ints))
        assert self.read() == "1"

    def handle_case(self, _i):
        # 2**7 = 128, so each R_i is 7 digits
        # int(56/(i+1)):[56, 28, 18, 14, 11, 9]
        g1 = self.query(56)
        self.debug(g1)
        r1 = int(g1[63 - 56 - 7 : 63 - 56], 2)
        r2 = int(g1[(63 - 28) - 7 : (63 - 28)], 2)
        self.debug(r1, r2)
        # int(170/(i+1)): [170, 85, 56, 42, 34, 28]
        g2 = self.query(170)
        self.debug(g2)
        r3 = int(g2[63 - 56 - 7 : 63 - 56], 2)
        r4 = int(g2[(63 - 42) - 7 : (63 - 42)], 2)
        self.debug(r3, r4)
        r5_plus_leading_r6_digit = int(g2[-42:-34], 2)
        self.debug(g2[-42:-34])
        self.debug(g2[-34:-28])
        r6_mod_64 = int(g2[-34:-28], 2)
        self.debug(r5_plus_leading_r6_digit, r6_mod_64)
        # Is r6 < 64?
        sum1 = int(g1[-25:-9], 2)
        sum2 = (
            (2 ** 9) * r3
            + (2 ** 5) * r4
            + (2 ** 2) * r5_plus_leading_r6_digit
            + r6_mod_64
        )
        self.debug(g1[-25:-9])
        self.debug("{0:b}".format(sum2))
        if sum1 == sum2:
            self.guess([r1, r2, r3, r4, r5_plus_leading_r6_digit, r6_mod_64])
        else:
            self.debug("branch 2")
            self.guess([r1, r2, r3, r4, r5_plus_leading_r6_digit - 1, 64 + r6_mod_64])


CaseHandler().run()
