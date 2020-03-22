"""
Savng universe
https://code.google.com/codejam/contest/32013/dashboard
12:39
12:55
"""


def solve_case(engines, queries):
    switches = 0
    used_engines = set(engines)
    for query in queries:
        if query in used_engines:
            used_engines.remove(query)
        if not used_engines:
            switches += 1
            used_engines = set(engines)
            used_engines.remove(query)
    return switches


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        s = int(input())
        engines = []
        for _ in range(s):
            engines.append(input())
        q = int(input())
        queries = []
        for _ in range(q):
            queries.append(input())
        soln = solve_case(engines, queries)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
