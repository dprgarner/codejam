from codejam import CodeJamParser


class Ovation(CodeJamParser):
    """
    2015, Qualification round, A
    https://code.google.com/codejam/contest/6224486/dashboard
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            case_line = next(self.source)
            _, shynesses_str = case_line.split(' ')
            yield [int(c) for c in list(shynesses_str)],

    def handle_case(self, shyness_count):
        partial_sums = [
            sum(shyness_count[:i])
            for i in range(1, len(shyness_count) + 1)
        ]

        return max([
            1 + i - partial_sums[i]
            for i in range(len(partial_sums))
        ] + [0])


if __name__ == '__main__':
    Ovation()