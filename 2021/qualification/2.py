"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145
"""


def solve_case(x, y, str_):
    current = None
    count_x = 0
    count_y = 0
    for s in reversed(str_):
        if current == "J" and s == "C":
            count_x += 1
        elif current == "C" and s == "J":
            count_y += 1

        if s != "?":
            current = s
    return count_x * x + count_y * y


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        x, y, str_ = (x for x in input().split(" "))
        x, y = int(x), int(y)
        assert x > 0
        assert y > 0
        soln = solve_case(x, y, str_)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
