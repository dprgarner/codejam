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

    def debug(self, *txt):
        # Uncomment for debugging.
        return
        print(*[str(t) for t in txt], file=sys.stderr)

    def handle_case(self, i):
        raise NotImplementedError


class CaseHandler(BaseInteractiveCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e05

    Practice, ~35m, 1 incorrect
    """

    def handle_case(self, i):
        n = int(self.read())
        words = [self.read() for _ in range(n)]
        soln = self.solve(words)
        self.write('Case #{}: {}'.format(i, soln))

    def solve(self, raw_words):
        words = sorted([w[::-1] for w in raw_words])
        # In python, '' is sorted before 'A'.
        self.debug(words)
        for accent_l in range(max(len(w) for w in words) - 1, 0, -1):
            self.debug(accent_l)
            i = len(words) - 2
            while i >= 0:
                self.debug('i', i)
                self.debug(words)
                self.debug(' ', i, words[i][:accent_l], words[i+1][:accent_l])
                if words[i][:accent_l] == words[i+1][:accent_l]:
                    stem = words[i][:accent_l]
                    x = words.pop(i)
                    y = words.pop(i)
                    self.debug('removed ', x, y)
                    i -= 1
                    while i >= 0 and words[i][:accent_l] == stem:
                        i -= 1
                i -= 1

        return len(raw_words) - len(words)


CaseHandler().run()
