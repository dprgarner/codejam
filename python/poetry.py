import math
from codejam import CodeJamParser


class Poetry(CodeJamParser):
    """
    2015, Qualification round, A
    https://code.google.com/codejam/contest/3264486/dashboard
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            yield int(next(self.source)),

    def handle_case(self, N):
        if N < 10:
            return N
        digits = len(str(N))

        # Steps to get to 10**digits
        steps_to_get_to_digits = 0
        for i in range(1, digits):
            steps_to_get_to_digits += 10**math.floor(i / 2) + 10**math.ceil(i / 2) - 1

        digits_str = str(N)
        # Formula works for odd or even number, too.
        first_half_reversed = int(''.join(list(reversed(digits_str[0:len(digits_str)//2])) ))
        second_half = int(digits_str[digits//2:])
        if first_half_reversed == 1:
            # Don't need to reverse at all.
            return steps_to_get_to_digits + second_half
        return  first_half_reversed + second_half + steps_to_get_to_digits


if __name__ == '__main__':
    Poetry()