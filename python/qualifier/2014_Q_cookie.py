from math import ceil
from codejam import CodeJamParser

# 19:08 - 19:36

class Run(CodeJamParser):
    """
    2014, Qualification round, B
    https://code.google.com/codejam/contest/2974486/dashboard#s=p0
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            c, f, x = [
                float(n) for n in next(self.source).split(' ')
            ]
            yield c, f, x

    def handle_case(self, c, f, x):
        # Required cookie-production speed:
        m = f * (x / c - 1)
        farms = max(0, ceil((m - 2) / f))
        t = 0
        for i in range(farms):
            speed = 2 + i * f
            t += c / speed
        t += x / (2 + farms * f)
        return t


if __name__ == '__main__':
    Run()
