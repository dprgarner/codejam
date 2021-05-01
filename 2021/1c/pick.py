"""
https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f00
"""
from math import ceil


def solve_case(k, ints):
    ints = sorted(ints)
    # open ends
    max_with_one_per_interval = []
    max_with_two_per_interval = [0]

    max_with_one_per_interval.append(ints[0] - 1)
    # I can pick 1 more, and then anything between ints[-1]+1 and k inclusive is a win
    max_with_one_per_interval.append(k - ints[-1])
    # print(sorted(ints))

    for i, j in zip(ints, ints[1:]):
        if i == j or i + 1 == j:
            continue

        # print("between ", i, "and", j)
        # print("max w/ two in int:", j - i - 1)
        max_with_two_per_interval.append(j - i - 1)

        # print("if just picking:", i + 1)

        # By picking i+1, I win i to first_loss, inclusive
        first_loss = ceil((j + i + 1) / 2)
        # print("I win:", first_loss - i - 1)

        max_with_one_per_interval.append(first_loss - i - 1)

    max_score_one = sum(sorted(max_with_one_per_interval)[-2:])
    max_score_two = max(max_with_two_per_interval)

    return max([max_score_one, max_score_two]) / k


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n, k = (int(x) for x in input().split(" "))
        ints = list(int(x) for x in input().split(" "))
        soln = solve_case(k, ints)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
