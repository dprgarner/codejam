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


def check_soln(year, soln):
    candidate = year + 1
    for candidate in range(year + 1, soln):
        assert not is_roaring(candidate)
    assert is_roaring(soln)


# check_soln(2021, 2122)

# for l in range(1, 9):
candidates = []

for l in range(1, 10):
    c = 10 ** l
    x = c
    candidate = str(c)

    y = c
    candidate2 = str(candidate)
    while len(candidate2) < 18 and y > 1:
        y -= 1
        candidate2 = "{}{}".format(y, candidate2)
        candidates.append(candidate2)

    while len(candidate) < 18:
        x += 1
        candidate = "{}{}".format(candidate, x)
        candidates.append(candidate)
        y = c
        candidate2 = str(candidate)

        while len(candidate2) < 18 and y > 1:
            y -= 1
            candidate2 = "{}{}".format(y, candidate2)
            candidates.append(candidate2)


candidates = sorted(int(s) for s in candidates)
print(candidates)
