"""
Codejam boilerplate. Copy/paste this file with handle_case customised.
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

    def err(self, *args):
        """
        For debugging.
        """
        print(*(str(arg) for arg in args), file=sys.stderr)

    def run(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            self.handle_case(i)

    def handle_case(self, i):
        raise NotImplementedError


ROOT_2 = math.sqrt(2)
ROOT_3 = math.sqrt(3)

EPS = 10**-7


class CaseHandler(BaseCaseHandler):
    """
    https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/00000000000079cc
    """

    def handle_case(self, i):
        area = float(self.read())
        soln = self.solve(area)
        self.write('Case #{}:'.format(i))
        for (x, y, z) in soln:
            self.write('{} {} {}'.format(x, y, z))

    def approx(self, a, b):
        return abs(a - b) < EPS

    def solve_2d(self, target_area):
        """
        Rotate about an axis through two centres parallel to the ground.
        Max shadow that can be achieved from this is ROOT_2, when angle = PI / 4.
        """
        if self.approx(target_area, 1):
            return 0, 1

        if self.approx(target_area, ROOT_2):
            return 1 / ROOT_2, 1 / ROOT_2

        # 1 < target_area < ROOT_2
        # Interval bisection.
        min_sin, max_sin = 0, 1 / ROOT_2
        while True:
            trial_sin = (min_sin + max_sin) / 2
            trial_cos = math.sqrt(1 - trial_sin * trial_sin)
            # Trigonometry!
            calc_area = trial_sin + trial_cos
            # self.err(calc_area, min_sin, max_sin)
            if self.approx(target_area, calc_area):
                return trial_sin, trial_cos
            if calc_area < target_area:
                min_sin = trial_sin
            if calc_area > target_area:
                max_sin = trial_sin

    def get_2d_centers(self, sin, cos):
        return [
            [sin / 2, cos / 2, 0],
            [-cos / 2, sin / 2, 0],
            [0, 0, 0.5],
        ]

    def solve_3d(self, target_area):
        """
        Starting from the PI/4 rotation in the 2d case, rotate about the
        axis parallel to the ground through the two centre-points of two
        opposite edges.
        Max shadow is ROOT_3, when angle is sin^-1 (1/ROOT_3).
        """
        if self.approx(target_area, ROOT_2):
            return 0, 1

        if self.approx(target_area, ROOT_3):
            return 1 / ROOT_3, ROOT_2 / ROOT_3

        # ROOT_2 < target_area < ROOT_3
        # Interval bisection.
        # Some trigonometry => 0 < sin < 1 / ROOT_3
        min_sin, max_sin = 0, 1 / ROOT_3
        while True:
            calc_sin = (min_sin + max_sin) / 2
            calc_cos = math.sqrt(1 - calc_sin * calc_sin)
            # More trigonometry!
            calc_area = calc_sin + ROOT_2 * calc_cos
            # self.err(calc_area, min_sin, max_sin)
            if self.approx(target_area, calc_area):
                return calc_sin, calc_cos
            if calc_area < target_area:
                min_sin = calc_sin
            if calc_area > target_area:
                max_sin = calc_sin

    def get_3d_centers(self, sin, cos):
        return [
            [1 / (2 * ROOT_2), cos / (2 * ROOT_2), -sin / (2 * ROOT_2)],
            [-1 / (2 * ROOT_2), cos / (2 * ROOT_2), -sin / (2 * ROOT_2)],
            [0, sin / 2, cos / 2],
        ]

    def solve(self, area):
        if area < ROOT_2:
            s, c = self.solve_2d(area)
            return self.get_2d_centers(s, c)

        s, c = self.solve_3d(area)
        return self.get_3d_centers(s, c)


CaseHandler().run()
