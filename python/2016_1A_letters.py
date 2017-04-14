from codejam import CodeJamParser

class Letters(CodeJamParser):
    """
    Q1, Round 1A, 2016 (Practice)
    https://code.google.com/codejam/contest/4304486/dashboard
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            letters = next(self.source)
            yield letters,

    def handle_case(self, letters):
        total = ""
        for letter in letters:
            option1 = total + letter
            option2 = letter + total
            total = option2 if option1 < option2 else option1
        return total


if __name__ == '__main__':
    Letters()