from os import sys

import math


ROOT_2 = 1.414213


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
            result_str = '\n'.join(
                ' '.join('{}'.format(f) for f in p)
                for p in result
            )
            self.dest.write('Case #{}:\n{}\n'.format(i + 1, result_str))


class CodeJam(CodeJamParser):
    """
    2018, Qualification round, D
    https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard
    Only works for the first half :(
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            yield float(next(self.source)),

    def handle_case(self, area):
        if area <= ROOT_2:
            # Easy case: one rotation.
            c_theta = (area + math.sqrt(2 - area ** 2)) / 2
            s_theta = math.sqrt(1 - c_theta ** 2)
            p1 = (0.5, 0, 0)
            p2 = (0, 0.5 * c_theta, 0.5 * s_theta)
            p3 = (0, -0.5 * s_theta, 0.5 * c_theta)
            return p1, p2, p3

        # Not finished this yet :(
        return (
            (0.5, 0, 0),
            (0, 0.5, 0),
            (0, 0, 0.5)
        )


CodeJam()
