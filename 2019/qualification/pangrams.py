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


class CaseHandler(BaseInteractiveCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
    """

    def handle_case(self, i):
        n, l = (int(x) for x in self.read().split(' '))
        # Prime products
        pps = [int(x) for x in self.read().split(' ')]
        # assert len(pps) == l
        soln = self.solve(n, pps)
        self.write('Case #{}: {}'.format(i, soln))

    def gcd(self, a, b):
        # Get greatest common divisor of two integers
        # a = q*b + r
        assert a
        assert b
        if a < b:
            return self.gcd(b, a)
        r = a % b
        # q = a // b
        # print('{} = {}*{} + {}'.format(a, q, b, r))
        if r == 0:
            return b
        return self.gcd(b, r)

    def get_pairs(self, pps):
        pairs = [None] * len(pps)
        # i is the first index where subsequent numbers are not equal
        for i in range(len(pps)):
            if pps[i] != pps[i+1]:
                break

        p = self.gcd(pps[i], pps[i+1])
        pairs[i] = (pps[i] // p, p)

        for j in range(i, 0, -1):
            pairs[j - 1] = pps[j - 1] // pairs[j][0], pairs[j][0]

        for j in range(i, len(pps) - 1):
            pairs[j + 1] = pairs[j][1], pps[j + 1] // pairs[j][1]

        return pairs

    def get_cypher(self, primes):
        assert len(primes) == 26, len(primes)
        dict_ = {}
        for i, x in enumerate(sorted(primes)):
            dict_[x] = chr(ord('A') + i)
        return dict_

    def solve(self, n, pps):
        pairs = self.get_pairs(pps)
        primes = set([x for x, _ in pairs] + [pairs[-1][1]])
        cypher = self.get_cypher(primes)
        chars = [cypher[p] for p, _ in pairs] + [cypher[pairs[-1][1]]]
        return ''.join(chars)


CaseHandler().run()
