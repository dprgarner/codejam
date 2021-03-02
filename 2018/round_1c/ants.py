"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000007765/000000000003e0a8
"""
from math import inf


def solve_case(weights):
    min_weight_by_stack_size = [0] + [inf] * len(weights)

    max_stack_size = 0
    for weight in weights:
        for stack_size in range(max_stack_size, -1, -1):
            if min_weight_by_stack_size[stack_size] <= 6 * weight:
                min_weight_by_stack_size[stack_size + 1] = min(
                    min_weight_by_stack_size[stack_size + 1],
                    weight + min_weight_by_stack_size[stack_size],
                )
        if min_weight_by_stack_size[max_stack_size + 1] < inf:
            max_stack_size += 1

    return max_stack_size


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        input()
        weights = list(int(x) for x in input().split(" "))
        soln = solve_case(weights)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
