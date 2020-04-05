"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f
"""


def get_blocks(min_digit, chars):
    bool_or_nones = [None if x in ("(", ")") else (x >= min_digit) for x in chars]

    blocks = []
    end_block = None
    for idx in range(len(bool_or_nones) - 1, -1, -1):
        relevant = bool_or_nones[idx]
        if relevant == None:
            continue

        if relevant and end_block != None:
            continue
        elif not relevant and end_block == None:
            continue
        elif relevant and end_block == None:
            end_block = idx + 1
        elif not relevant and end_block != None:
            blocks.append((idx + 1, end_block))
            end_block = None

    if end_block:
        blocks.append((0, end_block))
    return blocks


def insert_pars_around_blocks(min_digit, chars):
    chars = [x for x in chars]
    for min_digit in range(1, 10):
        for (start, end) in get_blocks(min_digit, chars):
            chars.insert(end, ")")
            chars.insert(start, "(")
    return chars


def solve_case(digits):
    digits = insert_pars_around_blocks(1, digits)
    return "".join(str(x) for x in digits)


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        digits = list(int(x) for x in input())
        soln = solve_case(digits)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
