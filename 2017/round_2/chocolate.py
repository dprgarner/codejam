"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000201900/00000000002017f4
"""
import math


def solve_case(p, gs):
    remainders = {i: 0 for i in range(p)}
    count = 0
    for g in gs:
        remainders[g % p] += 1

    count += remainders[0]

    if p == 2:
        return count + math.ceil(remainders[1] / 2)

    if p == 3:
        # Match 1 and 2 up with each other first
        count += min(remainders[1], remainders[2])
        remaining = abs(remainders[1] - remainders[2])
        return count + math.ceil(remaining / 3)

    if p == 4:
        equiv_gs = []
        for _ in range(min(remainders[1], remainders[3])):
            equiv_gs.append(1)
            equiv_gs.append(3)

        for _ in range(remainders[2]):
            equiv_gs.append(2)

        for _ in range(abs(remainders[1] - remainders[3])):
            equiv_gs.append(1)  # Doesn't matter if 1s or 3s here

        tally = 0
        for x in equiv_gs:
            if tally == 0:
                count += 1
            tally = (tally + x) % 4

        return count


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        _, p = (int(x) for x in input().split(" "))
        gs = [int(x) for x in input().split(" ")]
        soln = solve_case(p, gs)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
