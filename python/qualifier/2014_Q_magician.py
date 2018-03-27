from codejam import CodeJamParser

#18:57 - 19:08

BAD = 'Bad magician!'
CHEAT = 'Volunteer cheated!'

class Run(CodeJamParser):
    """
    2014, Qualification round, A
    https://code.google.com/codejam/contest/2974486/dashboard#s=p0
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            row1 = int(next(self.source))
            grid1 = []
            for _ in range(4):
                grid1.append([int(c) for c in next(self.source).split(' ')])
            row2 = int(next(self.source))
            grid2 = []
            for _ in range(4):
                grid2.append([int(c) for c in next(self.source).split(' ')])

            yield row1, grid1, row2, grid2

    def handle_case(self, row1, grid1, row2, grid2):
        candidates = set(grid1[row1 - 1]).intersection(set(grid2[row2 - 1]))
        if len(candidates) == 1:
            return candidates.pop()
        if len(candidates) > 1:
            return BAD
        return CHEAT

if __name__ == '__main__':
    Run()
