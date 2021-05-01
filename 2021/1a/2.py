"""
Tried to modify to work with the bigger test sets, but it didn't work.
"""


def solve_case(primes):
    m = len(primes)
    if sum(n for _, n in primes) > 101:
        raise Exception("Nope. :(")

    target = sum(p * n for p, n in primes)

    ks = [0] * (m + 1)
    ps = (0,) + tuple(p for p, _ in primes)
    ns = (1,) + tuple(n for _, n in primes)
    print(ps, ks, ns)
    print("target:", target)

    best = 0
    while ks[0] == 0:
        lhs_prod = 1
        target_sum = 0

        for i in range(1, m + 1):
            lhs_prod *= ps[i] ** ks[i]
            print("adding:", ps[i] * ks[i], ps[i] ** ks[i])
            target_sum += ps[i] * ks[i] + ps[i] ** ks[i]
            print("prod;sum:", lhs_prod, target_sum)
        if target_sum == target:
            print("New candidate found:", lhs_prod, ks, target_sum)
            best = max(best, lhs_prod)

        if target_sum > target:
            print("Overshot; wrapping k")
            ks[-1] = 0
            ks[-2] += 1
        else:
            ks[-1] += 1

        for i in range(m, 0, -1):
            if ks[i] > ns[i]:
                ks[i] = 0
                ks[i - 1] += 1
        print(ks)

    return best


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        m = int(input())
        primes = []
        for _ in range(m):
            primes.append(tuple(int(x) for x in input().split(" ")))
        soln = solve_case(primes)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
