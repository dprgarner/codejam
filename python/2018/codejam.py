from os import sys


class CodeJamParser(object):
    """
    Copy/paste this file, extend this class overriding the methods get_cases and handle_case, and call CodeJam.

    Use this class by initialising at the top level and piping to stdin/stdout.
    """

    @staticmethod
    def get_lines_from_stdin():
        try:
            while True:
                yield input()
        except EOFError:
            pass

    def __init__(self):
        self.source = get_lines_from_stdin()
        self.dest = sys.stdout
        self.write_cases()

    def write_cases(self):
        for i, case in enumerate(self.get_cases()):
            result = self.handle_case(*case)
            self.dest.write('Case #{}: {}\n'.format(i + 1, result))


class CodeJam(CodeJamParser):
    """
    2018, Qualification round, A
    https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            _ = int(next(self.source))
            yield [int(x) for x in next(self.source).split(' ')]

    def handle_case(self, numbers):
        print(numbers)