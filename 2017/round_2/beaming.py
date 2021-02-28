"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000201900/0000000000201876
Practice. It didn't work, even in the small set. :(
"""


DIRECTIONS = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}

REFLECT = {
    "/": {"N": "E", "E": "N", "W": "S", "S": "W",},
    "\\": {"N": "W", "W": "N", "E": "S", "S": "E",},
}


def solve_case(grid):
    r = len(grid)
    c = len(grid[0])

    ray_cache = {}
    ends_in_beam_cache = {}

    def trace(i, j):
        if (i, j) in ray_cache:
            return ray_cache[(i, j)], ends_in_beam_cache[(i, j)]

        r = len(grid)
        c = len(grid[0])

        rays = {}
        ends_in_beam = {}

        for d in DIRECTIONS:
            rays[d] = []
            ends_in_beam[d] = False
            curr_d = d
            curr_i, curr_j = i, j

            while True:
                curr_i += DIRECTIONS[curr_d][0]
                curr_j += DIRECTIONS[curr_d][1]
                if curr_i < 0 or curr_i == r or curr_j < 0 or curr_j >= c:
                    break
                rays[d].append((curr_i, curr_j))
                if grid[curr_i][curr_j] == "#":
                    break
                if grid[curr_i][curr_j] in ["|", "-"]:
                    ends_in_beam[d] = True
                    break
                if grid[curr_i][curr_j] in ["/", "\\"]:
                    curr_d = REFLECT[grid[curr_i][curr_j]][curr_d]

        ray_cache[(i, j)], ends_in_beam_cache[(i, j)] = rays, ends_in_beam

        return ray_cache[(i, j)], ends_in_beam_cache[(i, j)]

    def get_dir_traversing(i, j, k, l):
        # Which direction does a ray from i,j cross k,l?
        rays, _ = trace(i, j)
        for d, ray in rays.items():
            for p, q in ray:
                if (p, q) == (k, l):
                    return d

    orientables = []
    guaranteed_beams = [[0 for c in range(c)] for _ in range(r)]
    empties = []

    orientables_at_end = [[[] for c in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if grid[i][j] == ".":
                empties.append((i, j))
            if grid[i][j] in ["-", "|"]:
                rays, ends_in_beam = trace(i, j)
                can_be_horiz = not ends_in_beam["E"] and not ends_in_beam["W"]
                can_be_vert = not ends_in_beam["N"] and not ends_in_beam["S"]
                if can_be_horiz and can_be_vert:
                    orientables.append((i, j))
                    for d in DIRECTIONS:
                        for k, l in rays[d]:
                            if grid[k][l] == ".":
                                orientables_at_end[k][l].append((i, j))
                elif can_be_horiz and not can_be_vert:
                    grid[i][j] = "-"
                    for d in ["E", "W"]:
                        for k, l in rays[d]:
                            if grid[k][l] == ".":
                                guaranteed_beams[k][l] += 1
                elif not can_be_horiz and can_be_vert:
                    grid[i][j] = "|"
                    for d in ["N", "S"]:
                        for k, l in rays[d]:
                            if grid[k][l] == ".":
                                guaranteed_beams[k][l] += 1
                elif not can_be_horiz and not can_be_vert:
                    return None

    def fix_orientable(i, j, char):
        grid[i][j] = char

        # Get elts in and out of the ray, now.
        rays, _ = trace(i, j)
        elts_in_ray = []
        elts_off_ray = []
        for d in ["N", "S"]:
            if char == "|":
                elts_in_ray += rays[d]
            else:
                elts_off_ray += rays[d]
        for d in ["E", "W"]:
            if char == "|":
                elts_off_ray += rays[d]
            else:
                elts_in_ray += rays[d]

        # print("elts_in_ray", elts_in_ray)
        # print("elts_off_ray", elts_off_ray)
        # print("orientables:", orientables_at_end)
        for k, l in elts_in_ray:
            guaranteed_beams[k][l] += 1
        for k, l in elts_in_ray + elts_off_ray:
            # print(k, l)
            if grid[k][l] == ".":
                orientables_at_end[k][l].remove((i, j))

    while True:
        soln = True
        for i, j in empties:
            # print("empty:", i, j)
            # print("orientable thru it:", orientables_at_end[i][j])

            if guaranteed_beams[i][j] == 0:
                soln = False
                if len(orientables_at_end[i][j]) == 0:
                    # Cannot orient anything to go through this square
                    return None

                elif len(orientables_at_end[i][j]) == 1:
                    # Must reorient this one first.
                    k, l = orientables_at_end[i][j][0]
                    d = get_dir_traversing(k, l, i, j)
                    if d in ["N", "S"]:
                        fix_orientable(k, l, "|")
                    elif d in ["E", "W"]:
                        fix_orientable(k, l, "-")
                    else:
                        raise Exception("Something went wrong")
                    # Start again
                    break

        if soln:
            return grid

        # No empty point has a single potential orientable, now. So just fix one.
        for i, j in empties:
            if len(orientables_at_end[i][j]) == 2:
                # print("Here:", i, j)
                # print(grid)
                # print(orientables_at_end)
                # print(guaranteed_beams)
                k, l = orientables_at_end[i][j][0]
                fix_orientable(k, l, "|")
                # print("after:")
                # print(grid)
                # print(orientables_at_end)
                # print(guaranteed_beams)
                break

    # print(guaranteed_beams)
    # print(orientables_at_end)


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        r, _ = (int(x) for x in input().split(" "))
        grid = []
        for _ in range(r):
            grid.append([c for c in input()])
        soln = solve_case(grid)
        if soln:
            print("Case #{}: POSSIBLE".format(i), flush=True)
            for row in soln:
                print("".join(c for c in row), flush=True)
        else:
            print("Case #{}: IMPOSSIBLE".format(i), flush=True)


if __name__ == "__main__":
    run()
