"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000201900/0000000000201845
14:12-15:57.
Somehow, this lucky guess of a solution actually worked.
"""
import math


def solve_case(n, c, customers):
    # Keys are positions, then buyers
    customers_by_position = {}
    tickets_by_customer = {}
    for (p, b) in customers:
        if b not in tickets_by_customer:
            tickets_by_customer[b] = 0
        tickets_by_customer[b] += 1

        if p not in customers_by_position:
            customers_by_position[p] = {}
        if b not in customers_by_position[p]:
            customers_by_position[p][b] = 0
        customers_by_position[p][b] += 1

    # Get min trains
    subsums = [0]
    ratios = [-1]
    for i in range(1, c + 1):
        subsums.append(subsums[i - 1] + sum(customers_by_position.get(i, {}).values()))
        ratios.append(subsums[i] / i)
    # Minimise t s.t. ss[i] <= t*i
    min_trains = max(max(tickets_by_customer.values()), math.ceil(max(ratios)))

    # If it can be promoted, just promote it.
    min_promotions = 0
    for _, bs in customers_by_position.items():
        if sum(bs.values()) > min_trains:
            min_promotions += sum(bs.values()) - min_trains

    return min_trains, min_promotions


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n, c, m = (int(x) for x in input().split(" "))
        customers = []
        for _ in range(m):
            customers.append(tuple(int(x) for x in input().split(" ")))
        soln = solve_case(n, c, customers)
        print("Case #{}: {} {}".format(i, *soln), flush=True)


if __name__ == "__main__":
    run()
