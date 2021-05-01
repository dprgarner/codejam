"""
https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f01
"""


def is_roaring(year):
    digits = len(str(year))

    for l in range(1, digits):
        year_str = str(year)
        c = int(year_str[:l])

        candidate = str(c)
        while len(candidate) < digits:
            candidate = "{}{}".format(candidate, c + 1)
            c += 1
        if int(candidate) == year:
            return True
    return False


# def check_soln(year, soln):
#     candidate = year + 1
#     for candidate in range(year + 1, soln):
#         assert not is_roaring(candidate), "{} {} ... {}".format(year, soln, candidate)
#     assert is_roaring(soln)


def brute_force(year):
    candidate = year + 1
    while True:
        if is_roaring(candidate):
            return candidate
        candidate += 1


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        year = int(input())
        if year > 10 ** 6:
            raise Exception("nope.")

        soln = brute_force(year)
        # check_soln(year, soln)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
