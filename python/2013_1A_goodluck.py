import math
from codejam import CodeJamParser


def get_partitions(k, n):
    if k == 0:
        return []
    if k == 1:
        return [[n]]

    possible_partitions = []
    for a in range(0, n + 1):
        for subpartition in get_partitions(k - 1, a):
            possible_partitions.append(subpartition + [(n - a)])

    # Returns all possible non-negative sequences of
    # integers a_1,...a_k which sum to n.
    return possible_partitions


def factor_product(partition):
    factorials = [math.factorial(i) for i in partition]
    product = 1
    for i in factorials:
        product *= i
    return product


class GoodLuck(CodeJamParser):
    """
    Round 1A, 2013
    https://code.google.com/codejam/contest/2418487/dashboard

    I didn't get anywhere with this one. :( I read the solution. Something's
    still gone wrong, though :(( it only works for the small solution. A gold
    star to whoever figures it out.
    """
    def get_cases(self):
        _cases = int(next(self.source))  # 1
        r, n, m, k = [int(i) for i in next(self.source).split(' ')]
        factor_cases = []
        for row in range(r):
            factor_cases.append([int(i) for i in next(self.source).split(' ')])
        yield n, m, factor_cases

    memoised_products = {(): [1]}

    def get_products(self, subpartition):
        key = tuple(subpartition)
        if self.memoised_products.get(key):
            return self.memoised_products.get(key)
        head = subpartition[0]
        tail = subpartition[1:]
        subproducts = self.get_products(tail)
        self.memoised_products[key] = subproducts + [
            head * subproduct for subproduct in subproducts
        ]
        return self.memoised_products[key]

    possible_f_given_b = {}

    def get_hidden_set(self, partition):
        return [2 + i for i, j in enumerate(partition) for _ in range(j)]

    def handle_case(self, n, m, factor_cases):
        results = []
        self.partitions = [
            tuple(partition) for partition in get_partitions(m - 1, n)
        ]

        # Probability of a given partition b_i arising.
        self.prob_b = {}
        self.n = n
        self.m = m
        weight = math.factorial(n) / ((m-1)**n)
        for partition in self.partitions:
            self.prob_b[partition] = weight / factor_product(partition)

            hidden_set = self.get_hidden_set(partition)
            for product in self.get_products(hidden_set):
                if not self.possible_f_given_b.get(product):
                    self.possible_f_given_b[product] = {}
                self.possible_f_given_b[product][partition] = (
                    1 + self.possible_f_given_b[product].get(partition, 0)
                )

        for case in factor_cases:
            results.append(self.solve_row(case))
        return '\n'.join([''] + results)

    def solve_row(self, case):
        weight = 2 ** (self.n)
        possible_partitions = set(self.partitions)
        for product in case:
            possible_partitions = possible_partitions.intersection(
                self.possible_f_given_b[product].keys()
            )
        max_probability = 0  # Up to a 2**12 factor.
        for partition in possible_partitions:
            candidate = 1
            for product in case:
                candidate *= (self.possible_f_given_b[product][partition] / weight)
            candidate = candidate * self.prob_b[partition]
            if candidate > max_probability:
                max_probability = candidate
                max_partition = partition
        print('Chose:', max_partition, max_probability, '\n')

        return ''.join([str(x) for x in self.get_hidden_set(partition)])


if __name__ == '__main__':
    GoodLuck()