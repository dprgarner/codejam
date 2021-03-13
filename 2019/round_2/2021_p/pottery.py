"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/00000000001461c8#analysis

Adapted from the given solution.
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
        # self.debug("In: {}".format(input_))
        if input_ == "-1":
            raise WrongAnswerException
        return input_

    def write(self, txt):
        print(txt)
        # self.debug("Out: {}".format(txt))
        sys.stdout.flush()

    def debug(self, *txt):
        if not self.debug_mode:
            return
        print(*txt, file=sys.stderr)
        sys.stderr.flush()

    def run(self):
        cases = int(self.read())
        for i in range(1, cases + 1):
            self.handle_case()


class LastDayException(Exception):
    pass


class CaseHandler(BaseInteractiveCaseHandler):
    def read_day(self):
        self.day = int(self.read())
        if self.day == 100:
            raise LastDayException

    def inspect_vase(self, vase):
        self.debug("inspecting vase", vase)
        self.read_day()
        self.write("{} 0".format(vase))
        tokens = [int(x) for x in self.read().split(" ")[1:]]
        self.debug("Tokens in vase:", tokens)
        self.last_inspection[vase] = self.day
        self.known_counts[vase] = tokens
        return tokens

    def put_token(self, vase, player):
        self.debug("placing in vase:", vase, "token:", player)
        self.read_day()
        self.known_counts[vase].append(player)
        self.write("{} {}".format(vase, player))

    def is_valid(self, vase):
        tokens = self.known_counts[vase]
        for i, j in zip(tokens, tokens[1:]):
            if i == j:
                return False
        return True

    def handle_case(self):
        self.day = 0
        self.last_inspection = {i: 0 for i in range(1, 21)}
        self.known_counts = {i: [] for i in range(1, 21)}

        # Just sabotage the bad_vases for the first nights_before_inspect
        bad_vases = 10
        nights_before_inspect = 50

        try:
            for i in range(nights_before_inspect):
                vase = (i % bad_vases) + 1
                p = 1 + i // bad_vases
                self.put_token(vase, p)

            for i in range(1, 21):
                self.inspect_vase(i)

            candidate = -1
            smallest_token_count = 101
            for i in range(20, 0, -1):
                count = len(self.known_counts[i])
                if count < smallest_token_count and self.is_valid(i):
                    candidate = i
                    smallest_token_count = count

            # Sabotage everyone else but candidate
            while True:
                targets = [i for i in range(1, 21) if i != candidate]

                target = -1
                smallest_token_count = 101

                for i in reversed(targets):
                    count = len(self.known_counts[i])
                    if count < smallest_token_count:
                        target = i
                        smallest_token_count = count

                self.put_token(target, 1)

        except LastDayException:
            self.write("{} {}".format(candidate, 100))


CaseHandler().run()
