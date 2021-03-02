"""
Codejam boilerplate. Copy/paste this file with get_cases and handle_case
customised.

20:58-21:21. Damn. Should have picked this one.
"""
from os import sys
from math import inf


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
        if input_ == "-1":
            raise WrongAnswerException
        return input_

    def write(self, txt):
        print(txt)
        sys.stdout.flush()

    def debug(self, txt):
        if not self.debug_mode:
            return
        print(txt, file=sys.stderr)
        sys.stderr.flush()

    def run(self):
        (cases,) = (int(x) for x in self.read().split(" "))
        for i in range(1, cases + 1):
            self.handle_case(i)

    def handle_case(self, *args):
        raise NotImplementedError


class CaseHandler(BaseInteractiveCaseHandler):
    def get_order(self):
        response_ints = [int(x) for x in self.read().split(" ")]
        return response_ints

    def sell(self, data):
        self.write(data)

    def handle_case(self, _i):
        N = int(self.read())

        known_flavors = {}
        given_flavors = set()

        for _ in range(N):
            _, *flavors = self.get_order()

            for flavor in flavors:
                if flavor not in known_flavors:
                    known_flavors[flavor] = 0
                known_flavors[flavor] += 1

            # Pick the probably-least-popular one
            candidate_flavor = -1
            candidate_count = inf
            for flavor, count in known_flavors.items():
                if (
                    flavor not in given_flavors
                    and count < candidate_count
                    and flavor in flavors
                ):
                    candidate_flavor = flavor
                    candidate_count = count

            self.sell(candidate_flavor)
            given_flavors.add(candidate_flavor)


CaseHandler().run()
