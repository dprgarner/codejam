"""
Codejam boilerplate. Copy/paste this file with get_cases and handle_case
customised.
"""
from os import sys
import math


class BaseCaseHandler():
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

    def debug(self, *txt):
        # Uncomment for debugging.
        return
        print(*[str(t) for t in txt], file=sys.stderr)

    def run(self):
        cases, self.n, self.m = (int(x) for x in self.read().split(' '))
        for i in range(1, cases + 1):
            try:
                self.handle_case(i)
            except WrongAnswerException:
                self.debug('Wrong answer')
                return

    def handle_case(self, i):
        raise NotImplementedError


class WrongAnswerException(Exception):
    pass


# http://gauss.math.luc.edu/greicius/Math201/Fall2012/Lectures/ChineseRemainderThm.article.pdf
coprimes = (3, 5, 7, 11, 13, 16, 17)


def invert(m, mod):
    # Small enough to do by exhaustion
    trial = m
    while (trial * m) % mod != 1:
        trial = (trial * m) % mod
    return trial


def get_crt_args(coprimes):
    M = 1
    for coprime in coprimes:
        M *= coprime
    Ms = [M // coprime for coprime in coprimes]
    mod_Ms = [m % coprime for m, coprime in zip(Ms, coprimes)]
    ys = [invert(m, coprime) for m, coprime in zip(mod_Ms, coprimes)]
    args = [m * y for m, y in zip(Ms, ys)]
    return {
        coprime: arg
        for coprime, arg in zip(coprimes, args)
    }


crt = get_crt_args(coprimes)


class CaseHandler(BaseCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104f1a
    Practice, ~1h, no incorrects
    """

    def set_blades(self, blade_numbers):
        output = ' '.join('{}'.format(b) for b in blade_numbers)
        self.debug('output:', output)
        self.write(output)
        rotations = [int(x) for x in self.read().split(' ')]
        self.debug('rotations:', output)
        return rotations

    def solve_congruences(self, eqns):
        M = 1
        for coprime in coprimes:
            M *= coprime
        res = 0
        for coprime, n in eqns.items():
            self.debug(coprime, n)
            res += n * crt[coprime]
        return res % M

    def handle_case(self, _):
        results = {}
        for coprime in coprimes:
            blade_numbers = [coprime] * 18
            rotations = self.set_blades(blade_numbers)
            results[coprime] = sum(rotations) % coprime
        self.debug(results)
        soln = self.solve_congruences(results)
        self.write(soln)
        verdict = int(self.read())
        if verdict == -1:
            raise WrongAnswerException()
        self.debug('OK')


CaseHandler().run()
