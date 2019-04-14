from codejam import CodeJamParser

class BFFs(CodeJamParser):
    """
    Q3, Round 1A, 2016 (Practice)
    https://code.google.com/codejam/contest/4304486/dashboard#s=p2

    ... it's not the prettiest of code, but it works.
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            _n = int(next(self.source))
            bffs_str = next(self.source)
            yield [int(bff) for bff in bffs_str.split(' ')],

    def handle_case(self, bffs):
        # Build the mapping as a dict.
        mapping = {}
        n = len(bffs)
        for i, dest in enumerate(bffs):
            mapping[i+1] = dest

        # First, find the largest cycle.
        # Assign k:v to this when we find whether k is in a cycle of size v.
        # Assign k: -1 if k is not in a cycle.
        largest_cycles = {}

        for index in range(1, n + 1):
            cycle = []
            if largest_cycles.get(index):
                continue

            while index not in cycle:
                if largest_cycles.get(index):
                    # None of the entries in the list form a cycle.
                    for i in cycle:
                        largest_cycles[i] = -1
                    break
                cycle.append(index)
                index = mapping.get(index)

            if largest_cycles.get(index):
                continue

            # Numbers to right are in the cycle, numbers to the left are not.
            cutoff_index_for_cycle = cycle.index(index)
            for i in cycle[:cutoff_index_for_cycle]:
                largest_cycles[i] = -1
            actual_cycle = cycle[cutoff_index_for_cycle:]
            for i in actual_cycle:
                largest_cycles[i] = len(actual_cycle)

        largest_cycle = max(largest_cycles.values())

        # Next, find paths which end in a 2-cycle. Also record the 2-cycle
        # indices at the end of these paths.
        largest_paths = {}
        potential_path_starts = [k for k, v in largest_cycles.items() if v == -1]
        destination_2_cycles = {}

        for start in potential_path_starts:
            path = []
            index = start
            while largest_cycles.get(index) != 2:
                if largest_cycles.get(index) > 2:
                    # The path does not end in a 2-cycle.
                    for i in path:
                        largest_paths[i] = -1
                    break
                path.append(index)
                index = mapping.get(index)

            if largest_paths.get(start) != -1:
                # Path has ended in the 2-cycle at (index)
                for path_partial_length, pos in enumerate(reversed(path)):
                    largest_paths[pos] = 1 + path_partial_length
                    destination_2_cycles[pos] = index

        # Find all 2-cycles
        two_cycles = [
            (a, mapping[a])
            for a in range(1, n+1)
            if largest_cycles[a] == 2
            and a < mapping[a]
        ]
        # Find the maximum length of the paths which end at each side of the
        # 2-cycle, to find the largest 'double-path' ending in a 2-cycle at
        # both ends. Sum these all together to find the largest total size of
        # the circle when all the paths are 2-cycle paths.
        ending_in_2_cycles_total = 0
        for (i, j) in two_cycles:
            ending_in_i = [
                x for x, y in destination_2_cycles.items() if y == i
            ]
            ending_in_j = [
                x for x, y in destination_2_cycles.items() if y == j
            ]
            max_i_path = 0
            max_j_path = 0
            for x in ending_in_i:
                max_i_path = max(max_i_path, largest_paths[x])
            for x in ending_in_j:
                max_j_path = max(max_j_path, largest_paths[x])
            length_of_2_cycle_path = 2 + max_i_path + max_j_path
            ending_in_2_cycles_total += length_of_2_cycle_path
        return max(largest_cycle, ending_in_2_cycles_total)


if __name__ == '__main__':
    BFFs()