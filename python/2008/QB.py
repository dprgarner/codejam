"""
https://code.google.com/codejam/contest/32013/dashboard#s=p1
13:17 - 13:53
"""


def solve_case(abtrips, batrips):
    a = {}
    b = {}
    for (dep, arr) in abtrips:
        a[dep] = a.get(dep, 0) - 1
        b[arr] = b.get(arr, 0) + 1
    for (dep, arr) in batrips:
        b[dep] = b.get(dep, 0) - 1
        a[arr] = a.get(arr, 0) + 1

    a_min = 0
    a_total = 0
    for t in sorted(a.keys()):
        a_total += a[t]
        a_min = min(a_min, a_total)
    b_min = 0
    b_total = 0
    for t in sorted(b.keys()):
        b_total += b[t]
        b_min = min(b_min, b_total)
    return (-a_min, -b_min)


def toint(timestr):
    hours, mins = timestr.split(":")
    return int(hours) * 60 + int(mins)


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        t = int(input())
        na, nb = (int(x) for x in input().split(" "))
        abtrips = []
        for _ in range(na):
            dep, arr = input().split(" ")
            abtrips.append((toint(dep), toint(arr) + t))
        batrips = []
        for _ in range(nb):
            dep, arr = input().split(" ")
            batrips.append((toint(dep), toint(arr) + t))

        soln = solve_case(abtrips, batrips)
        print("Case #{}: {} {}".format(i, *soln), flush=True)


if __name__ == "__main__":
    run()
