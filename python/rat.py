from codejam import CodeJamParser
import math


def get_min(package_size, ingredient):
    return math.ceil(10 * package_size / (11 * ingredient))

def get_max(package_size, ingredient):
    return math.floor(10 * package_size / (9 * ingredient))

class Ratatouille(CodeJamParser):
    """
    Round 1A, 2017 (Practice)
    https://code.google.com/codejam/contest/5304486/dashboard#s=p1&a=0
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            rows = []
            n, p = [int(s) for s in next(self.source).split(' ')]
            ingredients = [int(s) for s in next(self.source).split(' ')]
            package_sizes = []
            for _ in range(n):
                package_sizes.append(
                  [int(x) for x in next(self.source).split(' ')]
                )
            yield (ingredients, package_sizes)

    def handle_case(self, ingredients, package_sizes):
        n = len(ingredients)
        p = len(package_sizes[0])

        # For each package, get max and min servings possible.
        servings_ranges = []
        for i in range(n):
            servings_ranges.append([])
            for j in range(p):
                min_servings = get_min(package_sizes[i][j], ingredients[i])
                max_servings = get_max(package_sizes[i][j], ingredients[i])
                # In some cases, min_servings > max_servings. These cases will
                # never make it into a kit, and the while loop accounts for
                # this.
                servings_ranges[i].append((min_servings, max_servings))
            servings_ranges[i] = sorted(servings_ranges[i])

        print (servings_ranges)
        kits = 0
        while all([bool(packages) for packages in servings_ranges]):
            # Start from the first column, find if an integer lies in all
            # ranges.
            min_servings = max([
                packages[0][0]
                for packages in servings_ranges
            ])
            max_servings = min([
                packages[0][1]
                for packages in servings_ranges
            ])
            if min_servings <= max_servings:
                # It's a kit: remove this column.
                kits += 1
                for packages in servings_ranges:
                    packages.pop(0)
            else:
                # There are entries which can't form a kit: remove the
                # smallest ones.
                for packages in servings_ranges:
                    min_, max_ = packages[0]
                    if max_ < min_servings:
                        packages.pop(0)
        return str(kits)


if __name__ == '__main__':
    Ratatouille()