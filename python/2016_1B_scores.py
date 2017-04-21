from codejam import CodeJamParser


def print_digits(c_digits, j_digits):
    c_str = str(''.join(str(c) for c in c_digits))
    j_str = str(''.join(str(j) for j in j_digits))
    return c_str + ' ' + j_str


def maxi_min(c_digits, j_digits, is_c_larger):
    length = len(c_digits)
    replace_c_with = 0 if is_c_larger else 9
    replace_j_with = 9 if is_c_larger else 0
    for j in range(length):
        c_digits[j] = c_digits[j] if c_digits[j] != -1 else replace_c_with
        j_digits[j] = j_digits[j] if j_digits[j] != -1 else replace_j_with
    return c_digits, j_digits


def add_digits_to_choices(first_c, first_j, choices):
    if not choices:
        return [([first_c], [first_j])]
    return [
        ([first_c] + new_c_digits, [first_j] + new_j_digits)
        for new_c_digits, new_j_digits in choices
    ]


def find_choices(input_c_digits, input_j_digits):
    c_digits, j_digits = [c for c in input_c_digits], [j for j in input_j_digits]
    length = len(c_digits)

    # Brute force approach
    # if not input_j_digits:
    #     return []
    # c_choices = [c_digits[0]] if c_digits[0] != -1 else range(10)
    # j_choices = [j_digits[0]] if j_digits[0] != -1 else range(10)
    # choices = []
    # for c in c_choices:
    #     for j in j_choices:
    #         choices.extend(add_digits_to_choices(c, j, find_choices(
    #             c_digits[1:], j_digits[1:]
    #         )))
    # return choices

    if not c_digits:
        return []

    if c_digits[0] == j_digits[0] and c_digits[0] != -1:
        return add_digits_to_choices(c_digits[0], j_digits[0], find_choices(
            c_digits[1:], j_digits[1:]
        ))

    if c_digits[0] != -1 and j_digits[0] != -1 and c_digits[0] != j_digits[0]:
        # maxi-min, they're different.
        return [maxi_min(c_digits[0:], j_digits[0:], c_digits[0:] > j_digits[0:])]

    # or c_digits[i] != -1 and j_digits[i] == -1
    # Options are: diff by one and maxi_min,
    # or set them equal and get more choices.
    if c_digits[0] == -1 and j_digits[0] != -1:
        choices = []
        differences = filter(
            lambda x: x >= 0 and x < 10,
            [j_digits[0] + x for x in [-1, 1]]
        )
        for diff in differences:
            choices.append(maxi_min(
                [diff] + c_digits[1:], j_digits[0:], diff > j_digits[0]
            ))
        choices.extend(
            add_digits_to_choices(j_digits[0], j_digits[0], find_choices(
                c_digits[1:], j_digits[1:]
            ))
        )
        return choices

    if c_digits[0] != -1 and j_digits[0] == -1:
        choices = []
        differences = filter(
            lambda x: x >= 0 and x < 10,
            [c_digits[0] + x for x in [-1, 1]]
        )
        for diff in differences:
            choices.append(maxi_min(
                c_digits[0:], [diff] + j_digits[1:], c_digits[0] > diff
            ))
        choices.extend(
            add_digits_to_choices(c_digits[0], c_digits[0], find_choices(
                c_digits[1:], j_digits[1:]
            ))
        )
        return choices

    if c_digits[0] == -1 and j_digits[0] == -1:
        #0,0 or 0,1 or 1,0... 
        choices = add_digits_to_choices(0, 0, find_choices(
            c_digits[1:], j_digits[1:]
        ))
        choices.append(maxi_min(
            [0] + c_digits[1:], [1] + j_digits[1:], False
        ))
        choices.append(maxi_min(
            [1] + c_digits[1:], [0] + j_digits[1:], True
        ))
        return choices

    raise Exception(input_c_digits, input_j_digits)


class Scores(CodeJamParser):
    """
    2017, Qualification round, A
    https://code.google.com/codejam/contest/3264486/dashboard
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            case_line = next(self.source)
            c, j = case_line.split(' ')
            c_digits = [-1 if s == '?' else int(s) for s in c]
            j_digits = [-1 if s == '?' else int(s) for s in j]
            yield c_digits, j_digits

    def handle_case(self, c_digits, j_digits):
        length = len(c_digits)

        choices = find_choices(c_digits, j_digits)
        min_diff = min_c = min_j = 10 ** (length + 1)

        for _c_digits, _j_digits in choices:
            c = int(''.join(str(x) for x in _c_digits))
            j = int(''.join(str(x) for x in _j_digits))
            diff = abs(c - j)
            if (
                diff < min_diff or (
                    diff == min_diff and (
                        c < min_c or (c == min_c and j < min_j)
                    )
                )
            ):
                min_c = c
                min_j = j
                min_diff = diff

        def scoreboard_print(n):
            digits = list(str(n))
            digits = [0] * (length - len(digits)) + digits
            return ''.join(str(c) for c in digits)

        return scoreboard_print(min_c) + ' ' + scoreboard_print(min_j)


if __name__ == '__main__':
    Scores()