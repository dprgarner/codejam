"""
One from the vaults.
https://code.google.com/codejam/contest/2270488/dashboard
"""

X_WON = "X won"
O_WON = "O won"
DRAW = "Draw"
INCOMPLETE = "Game has not completed"


def get_lines(rows):
    return (
        rows
        + [[rows[i][j] for i in range(4)] for j in range(4)]
        + [[rows[0][0], rows[1][1], rows[2][2], rows[3][3]]]
        + [[rows[0][3], rows[1][2], rows[2][1], rows[3][0]]]
    )


def get_winner(line):
    count = {
        "X": 0,
        "O": 0,
        "T": 0,
        ".": 0,
    }
    for col in line:
        count[col] += 1
    if count["X"] == 4 or count["X"] == 3 and count["T"] == 1:
        return X_WON
    if count["O"] == 4 or count["O"] == 3 and count["T"] == 1:
        return O_WON
    return None


def solve_case(rows):
    for line in get_lines(rows):
        winner = get_winner(line)
        if winner:
            return winner

    # No winning lines.
    for row in rows:
        for col in row:
            if col == ".":
                return INCOMPLETE
    return DRAW


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        rows = []
        for _ in range(4):
            rows.append([x for x in input()])
        input()

        soln = solve_case(rows)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
