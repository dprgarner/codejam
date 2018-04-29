from os import sys


class CodeJamParser(object):
    """
    Copy/paste this file, extend this class overriding the methods get_cases and
    handle_case, and call CodeJam.

    Use this class by initialising at the top level and piping to stdin/stdout.
    """

    @staticmethod
    def get_lines_from_stdin():
        try:
            while True:
                yield sys.stdin.readline()
        except EOFError:
            pass

    def __init__(self):
        self.source = self.get_lines_from_stdin()
        self.dest = sys.stdout
        self.write_cases()

    def write_cases(self):
        for i, case in enumerate(self.get_cases()):
            result = self.handle_case(*case)
            self.dest.write('Case #{}: {}\n'.format(i + 1, result))


class CodeJam(CodeJamParser):
    """
    2018, Qualification round, B
    https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            n = int(next(self.source))
            numbers_str = next(self.source).split(b' ')
            odd_numbers = []
            even_numbers = []
            for x in range(n):
                if x % 2 == 0:
                    even_numbers.append(int(numbers_str[x]))
                else:
                    odd_numbers.append(int(numbers_str[x]))
            yield odd_numbers, even_numbers

    def handle_case(self, odd_numbers, even_numbers):
        odd_numbers.sort()
        even_numbers.sort()
        try:
            i = 0
            while True:
                if even_numbers[i] > odd_numbers[i]:
                    return 2 * i
                if odd_numbers[i] > even_numbers[i + 1]:
                    return 2 * i + 1
                i += 1
        except IndexError:
            return 'OK'


CodeJam()
