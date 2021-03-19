"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000433651/0000000000433552
16:55 - 17:47.
"""

DIRECTION = {
    "^": (-1, 0),
    "<": (0, -1),
    ">": (0, 1),
    "v": (1, 0),
}


def solve_case(grid):
    r = len(grid)
    c = len(grid[0])

    def falls_off(i, j):
        delta = DIRECTION[grid[i][j]]

        while True:
            i += delta[0]
            j += delta[1]
            if i < 0 or i == r or j < 0 or j == c:
                return True
            if grid[i][j] != ".":
                return False

    count = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char != "." and falls_off(i, j):
                # Find an arrow it can point at.
                alternatives = list({"^", "v", "<", ">"}.difference(grid[i][j]))
                found = False
                while alternatives:
                    grid[i][j] = alternatives.pop()
                    if not falls_off(i, j):
                        found = True
                        break
                if not found:
                    return -1
                count += 1

    return count


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        r, c = (int(x) for x in input().split(" "))
        grid = []
        for _ in range(r):
            grid.append(list(c for c in (input())))
        soln = solve_case(grid)
        print(
            "Case #{}: {}".format(i, soln if soln != -1 else "IMPOSSIBLE"), flush=True
        )


if __name__ == "__main__":
    run()
