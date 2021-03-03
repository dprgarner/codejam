"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019ffb9/000000000033871f
"""
from math import inf
from fractions import Fraction


def solve_case(points):
    n = len(points)
    if n < 4:
        return n

    gradients = {inf: set()}
    for i in range(n):
        p, q = points[i]
        for j in range(i + 1, n):
            r, s = points[j]
            if p == r:
                grad = inf
            else:
                f = Fraction(s - q, r - p)
                # Indexing by tuple seems to work faster than comparing
                # on the Fraction class directly.
                grad = (f.numerator, f.denominator)
            if grad not in gradients:
                gradients[grad] = set()
            gradients[grad].update([i, j])

    max_colinear = -1
    max_grad = None
    for grad, colinear_pts in gradients.items():
        if len(colinear_pts) > max_colinear:
            max_colinear = len(colinear_pts)
            max_grad = grad

    remaining_pts = set(range(n)).difference(gradients[max_grad])

    return (
        max_colinear + min(2, len(remaining_pts))
        if max_colinear % 2 == 0
        else max_colinear + min(1, len(remaining_pts))
    )


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n = int(input())
        points = []
        for _ in range(n):
            points.append(tuple(int(x) for x in input().split(" ")))
        soln = solve_case(points)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
