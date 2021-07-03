"""
2017, Qualification round, A
https://code.google.com/codejam/contest/3264486/dashboard
"""

DIGITS = [
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE",
]

LEVELS = [
    {
        "Z": 0,
        "W": 2,
        "U": 4,
        "X": 6,
        "G": 8,
    },
    {
        "O": 1,
        "H": 3,
        "F": 5,
        "S": 7,
    },
    {
        "I": 9,
    },
]


def solve_case(phone_letters):
    numbers = []
    for level in LEVELS:
        for letter in level.keys():
            occurences = phone_letters.count(letter)
            number = level[letter]
            for _ in range(occurences):
                numbers.append(number)
                for x in DIGITS[number]:
                    phone_letters.remove(x)
    return "".join(str(s) for s in sorted(numbers))


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        soln = solve_case(list(input()))
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
