"""
s: 13:45ish
e: 14:21ish (small soln)
"""


def solve_case(sijs):
    total_interest = 0
    r = len(sijs)
    c = len(sijs[0])

    round_no = 0
    while True:
        round_no += 1
        # Tally up round first?
        for i in range(r):
            for j in range(c):
                total_interest += sijs[i][j] or 0

        neighbours = []
        for i in range(r):
            neighbours.append([])
            for _ in range(c):
                neighbours[i].append([])

        for i in range(r):
            for j in range(c):
                if sijs[i][j] is None:
                    continue
                # Get nearest neighbour in row
                for k in range(j + 1, c):
                    if sijs[i][k] is not None:
                        neighbours[i][k].append((i, j))
                        neighbours[i][j].append((i, k))
                        break
                # Get nearest neighbour in col
                for l in range(i + 1, r):
                    if sijs[l][j] is not None:
                        neighbours[i][j].append((l, j))
                        neighbours[l][j].append((i, j))
                        break

        elimination_this_round = False
        eliminations = []
        for i in range(r):
            eliminations.append([])
            for _ in range(c):
                eliminations[i].append(False)

        for i in range(r):
            for j in range(c):
                if sijs[i][j] is None:
                    continue
                if not neighbours[i][j]:
                    continue
                avg = sum(sijs[k][l] for (k, l) in neighbours[i][j]) / len(
                    neighbours[i][j]
                )
                if avg > sijs[i][j]:
                    elimination_this_round = True
                    eliminations[i][j] = True

        if not elimination_this_round:
            return total_interest

        for i in range(r):
            for j in range(c):
                if eliminations[i][j]:
                    sijs[i][j] = None


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        r, c = (int(x) for x in input().split(" "))
        sijs = []
        for _ in range(r):
            sijs.append(list(int(c) for c in input().split(" ")))
        soln = solve_case(sijs)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
