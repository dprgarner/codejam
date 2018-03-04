from codejam import CodeJamParser

class Soldiers(CodeJamParser):
    """
    Q2, Round 1A, 2016 (Practice)
    https://code.google.com/codejam/contest/4304486/dashboard#s=p1
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            rows = []
            n = int(next(self.source))
            for j in range(2 * n - 1):
                heights_str = next(self.source)
                rows.append([int(x) for x in heights_str.split(' ')])
            yield rows,

    def handle_case(self, rows):
        counts = {}
        for row in rows:
            for height in row:
                counts[height] = counts.get(height, 0) + 1
        missing_heights = sorted([k for k, v in counts.items() if v % 2 == 1])
        return ' '.join([str(h) for h in missing_heights])


if __name__ == '__main__':
    Soldiers()