import math
from codejam import CodeJamParser


def check(r, s, t):
    return 2 * (s ** 2) + (2 * r - 1) * s <= t


class Rings(CodeJamParser):
    """
    Round 1A, 2013
    https://code.google.com/codejam/contest/2418487/dashboard
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            case_line = next(self.source)
            r_str, t_str = case_line.split(' ')
            yield (int(r_str), int(t_str))

    def handle_case(self, r, t):
        discriminant = (2*r-1)**2 + 8 * t
        s = math.floor((-(2*r-1) + math.sqrt(discriminant)) / 4)
        # s is only approximate because of rounding errors... find the true
        # value.
        while True:
            if check(r, s, t) and check(r, s+1, t):
                s += 1
            elif not check(r, s, t) and not check(r, s+1, t): 
                s -= 1
            else:
                return s

if __name__ == '__main__':
    Rings()