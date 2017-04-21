from codejam import CodeJamParser

DIGITS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

LEVELS = [
    {
        'Z': 0,
        'X': 6,
        'G': 8,
    },
    {
        'W': 2,
        'H': 3,
        'U': 4,
        'S': 7,
    },
    {
        'O': 1,
        'F': 5,
    },
    {
        'I': 9,
    },
]


class Digits(CodeJamParser):
    """
    2017, Qualification round, A
    https://code.google.com/codejam/contest/3264486/dashboard
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            case_line = next(self.source)
            yield sorted(case_line),

    def handle_case(self, phone_letters):
        numbers = []
        for level in LEVELS:
            for letter in level.keys():
                occurences = phone_letters.count(letter)
                number = level[letter]
                for _ in range(occurences):
                    numbers.append(number)
                    for x in DIGITS[number]:
                        phone_letters.remove(x)
        return ''.join(str(s) for s in sorted(numbers))
    
if __name__ == '__main__':
    Digits()


