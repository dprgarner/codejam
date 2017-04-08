from codejam import CodeJamParser


def is_space_plus_only(grid, i, j):
    """
    i, j are between 0 and N-1 for a grid of size N.
    Returns true if only plus-models can go in this space.
    """
    n = len(grid)
    for y in range(n):
        if y == i:
            continue
        if grid[y][j] == 'x' or grid[y][j] == 'o':
            return True
    for x in range(n):
        if x == j:
            continue
        if grid[i][x] == 'x' or grid[i][x] == 'o':
            return True
    return False


def is_space_cross_only(grid, i, j):
    """
    i, j are between 0 and N-1 for a grid of size N.
    Returns true if only plus-models can go in this space.
    """
    n = len(grid)

    # Diagonal ending at the top-left
    offset = i - j
    t_i, t_j = (0, -offset) if offset < 0 else (offset, 0)
    for k in range(n - abs(offset)):
        x, y = t_i + k, t_j + k
        if x == i:
            continue
        if grid[x][y] == '+' or grid[x][y] == 'o':
            return True

    # Diagonal ending at the top-right
    offset = i + j
    t_i, t_j = (0, offset) if offset < n - 1 else (offset - n + 1, n - 1)

    for k in range(t_j - t_i + 1):
        x, y = t_i + k, t_j - k
        if x == i:
            continue
        if grid[x][y] == '+' or grid[x][y] == 'o':
            return True
    return False


def score_grid(grid):
    def score_element(c):
        if c == 'o':
            return 2
        if c == '+' or c == 'x':
            return 1
        return 0

    sum = 0
    n = len(grid)
    for i in range(n):
        for j in range(n):
            sum += score_element(grid[i][j]) 
    return sum

def _handle_case(grid):
    model_changes = []
    n = len(grid)
    for i in range(n):
        for j in range(n):
            plus_only = is_space_plus_only(grid, i, j)
            if plus_only and grid[i][j] == '+':
                continue
            cross_only = is_space_cross_only(grid, i, j)
            if cross_only and grid[i][j] == 'x':
                continue

            if not plus_only and not cross_only and grid[i][j] == 'o':
                continue
            if plus_only and cross_only:
                continue

            if plus_only and not cross_only:
                grid[i][j] = '+'
            elif not plus_only and cross_only:
                grid[i][j] = 'x'
            else:
                grid[i][j] = 'o'
            model_changes.append(
                '{} {} {}'.format(grid[i][j], str(i+1), str(j+1))
            )

    output = '\n'.join([
        '{} {}'.format(score_grid(grid), len(model_changes))
    ] + model_changes)

    return output



class Fashion(CodeJamParser):
    """
    2017, Qualification round, C
    https://code.google.com/codejam/contest/3264486/dashboard#s=p2
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            grid_size_str, models_str = next(self.source).split(' ')
            grid_size = int(grid_size_str)
            models = int(models_str)
            grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
            for j in range(models):
                model, row_str, col_str = next(self.source).split(' ')
                grid[int(row_str) - 1][int(col_str) - 1] = model
            yield grid,

    def handle_case(self, grid):
        return _handle_case(grid)


if __name__ == '__main__':
    Fashion()