from codejam import CodeJamParser


class Pancakes(CodeJamParser):
    """
    2017, Qualification round, A
    https://code.google.com/codejam/contest/3264486/dashboard
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            case_line = next(self.source)
            pancakes_str, flipper_size_str = case_line.split(' ')
            yield [c == '+' for c in list(pancakes_str)], int(flipper_size_str)

    def handle_case(self, pancakes, flipper_size):
        flips = 0
        for i in range(0, len(pancakes) - flipper_size + 1):
            if not pancakes[i]:
                flips += 1
                for j in range(flipper_size):
                    pancakes[i+j] = not pancakes[i+j]
        if all(pancakes):
            return flips
        return 'IMPOSSIBLE'


if __name__ == '__main__':
    Pancakes()