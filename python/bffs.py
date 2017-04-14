from codejam import CodeJamParser

class BFFs(CodeJamParser):
    """
    Q3, Round 1A, 2016 (Practice)
    https://code.google.com/codejam/contest/4304486/dashboard#s=p2
    """
    def get_cases(self):
        cases = int(next(self.source))
        for i in range(1, cases + 1):
            _n = int(next(self.source))
            bffs_str = next(self.source)
            yield [int(bff) for bff in bffs_str.split(' ')],

    def handle_case(self, bffs):
        # Build semipermutation as dict
        semiperm = {}
        n = len(bffs)
        for i, dest in enumerate(bffs):
            semiperm[i+1] = dest

        # First, find the largest cycle. Then, find largest path ending in 2-cycle.

        # Assign to this when we find the largest possible cycle for that entry.
        largest_cycles = {}

        for index in range(1, n + 1):
            cycle = []
            if largest_cycles.get(index):
                continue

            while index not in cycle:
                if largest_cycles.get(index):
                    # None of the entries in the list form a cycle here.
                    for i in cycle:
                        largest_cycles[i] = -1
                    break
                cycle.append(index)
                index = semiperm.get(index)

            if largest_cycles.get(index):
                continue

            # Numbers to right are in cycle, numbers left are not.
            cutoff_index_for_cycle = cycle.index(index)
            for i in cycle[:cutoff_index_for_cycle]:
                largest_cycles[i] = -1
            actual_cycle = cycle[cutoff_index_for_cycle:]
            for i in actual_cycle:
                largest_cycles[i] = len(actual_cycle)

        largest_cycle = max(largest_cycles.values())

        largest_paths = {}
        potential_path_starts = [k for k, v in largest_cycles.items() if v == -1]
        destination_2_cycles = {}

        # Find paths ending in 2-cycle
        for start in potential_path_starts:
            path = []
            index = start
            while largest_cycles.get(index) != 2:
                if largest_cycles.get(index) > 2:
                    # Not a valid path.
                    for i in path:
                        largest_paths[i] = -1
                    break
                path.append(index)
                index = semiperm.get(index)

            if largest_paths.get(start) != -1:
                # Path has ended in the 2-cycle at (index)
                for path_partial_length, pos in enumerate(reversed(path)):
                    largest_paths[pos] = 1 + path_partial_length
                    destination_2_cycles[pos] = index

        # Find all 2-cycles
        two_cycles = [
            (a, semiperm[a])
            for a in range(1, n+1)
            if largest_cycles[a] == 2
            and a < semiperm[a]
        ]

        # Find the length of all max paths that end in each side of the 2-cycle.
        ending_in_2_cycle_max = 0
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
            # print('ending_in_i', ending_in_i)
            # print('ending_in_j', ending_in_j)
            # print('max_i_path', max_i_path)
            # print('max_j_path', max_j_path)
            length_of_2_cycle_path = 2 + max_i_path + max_j_path
            ending_in_2_cycle_max += length_of_2_cycle_path
        # print (bffs)
        # print (semiperm)
        # print('largest_cycles:', largest_cycles)
        # print('largest_paths:', largest_paths)
        # print('destination_2_cycles', destination_2_cycles)
        # print('ending_in_2_cycle_max', ending_in_2_cycle_max)
        return max(largest_cycle, ending_in_2_cycle_max)




if __name__ == '__main__':
    BFFs()




# while index not in cycle:
#     if largest_cycles.get(index):
#         break
#     cycle.append(index)
#     index = semiperm.get(index)
# closed_cycle = bool(largest_cycles.get(index))

# for i in cycle:
#     largest_cycles[i] = (
#         len(cycle)
#         if closed_cycle
#         else largest_cycles.get(i, -1)
#     )






# for i in range(n):
#     if not semiperm:
#         break
#     index = i + 1
#     if not semiperm.get(index):
#         continue

#     start = index
#     cycle_size = 0
#     while index != start:
#         index = semiperm.get(index)
#         cycle_size += 1
#     if index == start:
#         max_cycle = max(max_cycle, cycle_size)