from codejam import CodeJamParser
import random


class Alphabet(CodeJamParser):
    """
    Round 1A, 2017 (Practice)
    https://code.google.com/codejam/contest/5304486/dashboard

    ... there has to be a better way to do this. It's very slow (~1minute)
    and quite volatile, and it took ages.
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            rows, cols = [int(s) for s in next(self.source).split(' ')]
            grid = []
            letters = {}
            unknowns = []
            for row in range(rows):
                row_string = next(self.source)
                for col, s in enumerate(row_string):
                    if s == '?':
                        unknowns.append((row, col))
                    else:
                        letters[s] = (row, col, row, col)  # Top left bottom right
                grid.append([s if s!='?' else None for s in row_string])
            yield grid, letters, unknowns

    def is_letter_available(self, grid, unknown, letter, letter_pos):
        # Find the smallest rectangle containing ? and each occurence
        # of the letter. If this contains any other letters, it can't
        # be that letter.
        (i, j) = unknown
        (top, left, bottom, right) = letter_pos

        rect_top = min(top, i)
        rect_left = min(left, j)
        rect_bottom = max(bottom, i)
        rect_right = max(right, j)
        # print (top, right, bottom, left)
        # print (rect_top, rect_left, rect_bottom, rect_right)
        for p in range(rect_top, rect_bottom + 1):
            for q in range(rect_left, rect_right + 1):
                if grid[p][q] and grid[p][q] != letter:
                    return False
        return True

    def fill_in_letter(self, grid, letters, unknowns, letter, pos):
        (i, j) = pos
        new_unknowns = [v for v in unknowns if v != (i, j)]
        new_grid = [[c for c in r] for r in grid]
        new_grid[i][j] = letter
        new_letters = {k: v for k, v in letters.items()}
        top, left, bottom, right = letters[letter]
        new_letters[letter] = (
            min(top, i),
            min(left, j),
            max(bottom, i),
            max(right, j)
        )
        top, left, bottom, right = new_letters[letter]
        for p in range(top, bottom + 1):
            for q in range(left, right + 1):
                new_grid[p][q] = letter
                if (p, q) in new_unknowns:
                    new_unknowns.remove((p, q))
        return new_grid, new_letters, new_unknowns

    def guess_a_letter(self, grid, letters, unknowns):
        choices_dict = {}
        for (i, j) in unknowns:
            choices_dict[(i, j)] = []
            for letter, pos in letters.items():
                if self.is_letter_available(grid, (i, j), letter, pos):
                    choices_dict[(i, j)].append(letter)

        # Fill in the entries with only one choice.
        candidates = {}
        # print (choices_dict)
        for (i, j), choices in choices_dict.items():
            if len(choices) == 0:
                # Something went wrong.
                return False, grid, letters, unknowns
            if len(choices) == 1:
                return (True, *self.fill_in_letter(
                    grid, letters, unknowns, choices[0], (i, j)
                ))

        # Fuck, just pick one.
        (i, j), choices = random.choice(list(choices_dict.items()))
        letter = random.choice(choices)
        return (True, *self.fill_in_letter(
            grid, letters, unknowns, letter, (i, j)
        ))

    def handle_case(self, grid, letters, unknowns):
        new_grid, new_letters, new_unknowns = grid, letters, unknowns
        while new_unknowns:
            (
                result,
                new_grid,
                new_letters,
                new_unknowns
            ) = self.guess_a_letter(new_grid, new_letters, new_unknowns)
            if not result:
                # Start again :( This seems to happen very rarely.
                new_grid, new_letters, new_unknowns = grid, letters, unknowns

        return '\n'+'\n'.join([''.join([c for c in row]) for row in new_grid])


if __name__ == '__main__':
    Alphabet()