"""
Codejam boilerplate. Copy/paste this file with get_cases and handle_case
customised.
"""
from os import sys


class WrongAnswerException(Exception):
    pass


class BaseInteractiveCaseHandler:
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
        input_ = next(self.source).strip()
        if input_ == "-1":
            raise WrongAnswerException
        return input_

    def write(self, *txt):
        print(*txt)
        sys.stdout.flush()

    def run(self):
        cases, self.n, self.q = (int(x) for x in self.read().split(" "))
        for i in range(1, cases + 1):
            self.handle_case()


class CaseHandler(BaseInteractiveCaseHandler):
    def query(self, i, j, k):
        self.write(" ".join(str(x) for x in (i, j, k)))
        response = int(self.read())
        return response

    def guess(self, guess_array):
        # Example method
        self.write(" ".join(str(x) for x in guess_array))
        assert self.read() == "1"

    def handle_case(self):
        current = {
            1: [2, 1, 3],
            2: [1, 2, 3],
            3: [1, 3, 2],
        }[self.query(1, 2, 3)]

        for i in range(4, self.n + 1):
            start = 0
            end = len(current) - 1

            while True:
                d = end - start
                lower_third = start + (d // 3)
                upper_third = start + (2 * d // 3)
                if lower_third == upper_third:
                    break

                m = self.query(i, current[lower_third], current[upper_third])
                if m == i:
                    start = lower_third
                    end = upper_third
                elif m == current[lower_third]:
                    end = lower_third
                elif m == current[upper_third]:
                    start = upper_third
                else:
                    raise Exception("something went wrong")

            if end <= 1:
                m = self.query(current[0], current[1], i)
                if m == i:
                    current.insert(1, i)
                elif m == current[0]:
                    current.insert(0, i)
                else:
                    raise Exception("something went wrong")
            elif upper_third >= len(current) - 2:
                m = self.query(current[-2], current[-1], i)
                if m == i:
                    current.insert(-1, i)
                elif m == current[-1]:
                    current.append(i)
                else:
                    raise Exception("something went wrong")
            else:
                current.insert(upper_third + 1, i)

        self.guess(current)


CaseHandler().run()
