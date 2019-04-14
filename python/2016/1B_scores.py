from codejam import CodeJamParser


def to_int(digits):
    return int(''.join(str(d) for d in digits))


def maxi_min(c_digits, j_digits):
    # Find where differ, fill in after, return ints.
    for index in range(len(c_digits)):
        if c_digits[index] != j_digits[index]:
            break
    is_c_larger = to_int(c_digits[:index+1]) > to_int(j_digits[:index+1])
    replace_c_with, replace_j_with = (
        (0, 9)
        if is_c_larger
        else (9, 0)
    )
    c = to_int(c_digits[:index+1] + [
        replace_c_with if d==-1 else d for d in c_digits[index+1:]
    ])
    j = to_int(j_digits[:index+1] + [
        replace_j_with if d==-1 else d for d in j_digits[index+1:]
    ])
    return (c, j)


def generate_choices(c_digits, j_digits):
    for index in range(len(c_digits)):
        c_digit = c_digits[index]
        j_digit = j_digits[index]                
        # print (c_digits, j_digits)
        if c_digit != -1 and j_digit != -1:
            if c_digit != j_digit:
                yield maxi_min(c_digits, j_digits)
                return
        elif c_digit == -1 and j_digit != -1:
            if j_digit < 9:
                yield maxi_min(
                    c_digits[:index] + [j_digit + 1] + c_digits[index+1:],
                    j_digits
                )
            if j_digit > 0:
                yield maxi_min(
                    c_digits[:index] + [j_digit - 1] + c_digits[index+1:],
                    j_digits
                )
            c_digits[index] = j_digit
        elif c_digit != -1 and j_digit == -1:
            if c_digit < 9:
                yield maxi_min(
                    c_digits,
                    j_digits[:index] + [c_digit + 1] + j_digits[index+1:]
                )
            if c_digit > 0:
                yield maxi_min(
                    c_digits,
                    j_digits[:index] + [c_digit - 1] + j_digits[index+1:]
                )
            j_digits[index] = c_digit
        else:
            yield maxi_min(
                c_digits[:index] + [1] + c_digits[index+1:],
                j_digits[:index] + [0] + j_digits[index+1:]
            )
            yield maxi_min(
                c_digits[:index] + [0] + c_digits[index+1:],
                j_digits[:index] + [1] + j_digits[index+1:]
            )
            c_digits[index] = j_digits[index] = 0
    yield (to_int(c_digits), to_int(j_digits))


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
        min_diff = min_c = min_j = 10 ** (length + 1)

        for c, j in generate_choices(c_digits, j_digits):
            # print ('yielded:', c, j)
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

        def zero_pad(n):
            n_length = len(str(n))
            return '0' * (length - n_length) + str(n)

        return zero_pad(min_c) + ' ' + zero_pad(min_j)


if __name__ == '__main__':
    Scores()