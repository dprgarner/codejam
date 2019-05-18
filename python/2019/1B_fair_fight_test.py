from unittest import TestCase, main

from _1B_fair_fight import MaxRangeTree, bisect

"""
class TestGetCappedPairsCount(TestCase):
    def test_get_capped_pairs_count_smoke_test(self):
        self.assertEqual(
            get_capped_pairs_count(3, [1, 1, 1, 8], [8, 8, 8, 8], 9), 4
        )
        self.assertEqual(get_capped_pairs_count(1, [0, 1, 1], [1, 1, 0], 2), 4)
        self.assertEqual(get_capped_pairs_count(2, [0, 1, 1], [1, 1, 0], 2), 1)
        self.assertEqual(get_capped_pairs_count(2, [0, 1, 1], [1, 1, 0], 1), 1)
        self.assertEqual(
            get_capped_pairs_count(0, [3], [3], 4), 1
        )
        self.assertEqual(
            get_capped_pairs_count(1, [0, 8, 0, 8, 0], [4, 0, 4, 0, 4], 9), 8
        )
        self.assertEqual(get_capped_pairs_count(
            1, [0, 8, 0, 8, 0], [4, 0, 4, 0, 4], 8
        ), 8)
        self.assertEqual(get_capped_pairs_count(
            3, [0, 8, 0, 8, 0], [4, 0, 4, 0, 4], 9
        ), 4)
        self.assertEqual(get_capped_pairs_count(
            3, [0, 8, 0, 8, 0], [4, 0, 4, 0, 4], 8
        ), 4)
        self.assertEqual(get_capped_pairs_count(0, [1, 0, 0], [0, 1, 2], 2), 2)
        self.assertEqual(get_capped_pairs_count(0, [1, 0, 0], [0, 1, 2], 1), 1)
        self.assertEqual(get_capped_pairs_count(
            2, [1, 2, 3, 4, 5], [5, 5, 5, 5, 10], 6), 3
        )
        self.assertEqual(get_capped_pairs_count(
            3, [1, 2, 3, 4, 5], [5, 5, 5, 5, 10], 7
        ), 4)

    def test_get_capped_pairs_alternating_first_index(self):
        cs = [0, 8, 0, 8, 0]
        ds = [4, 0, 4, 0, 4]
        self.assertEqual(get_capped_pairs_count(0, cs, ds, 0), 0)
        self.assertEqual(get_capped_pairs_count(0, cs, ds, 3), 0)
        self.assertEqual(get_capped_pairs_count(0, cs, ds, 4), 0)
        self.assertEqual(get_capped_pairs_count(0, cs, ds, 5), 1)
        self.assertEqual(get_capped_pairs_count(0, cs, ds, 8), 1)

    def test_get_capped_pairs_alternating_second_index(self):
        cs = [0, 8, 0, 8, 0]
        ds = [4, 0, 4, 0, 4]
        self.assertEqual(get_capped_pairs_count(1, cs, ds, 0), 0)
        self.assertEqual(get_capped_pairs_count(1, cs, ds, 3), 1)
        self.assertEqual(get_capped_pairs_count(1, cs, ds, 4), 1)
        self.assertEqual(get_capped_pairs_count(1, cs, ds, 5), 8)
        self.assertEqual(get_capped_pairs_count(1, cs, ds, 8), 8)
"""


class TestGetCappedPairsCount(TestCase):
    def test_lower_bisect(self):
        cs = [4, 3, 2, 3, 4]
        i = 2
        ctree = MaxRangeTree(cs)

        def lower_predicate(cap, s):
            return ctree.rmq(s, i) >= cap

        lower = bisect(0, i, lambda x: lower_predicate(1, x))
        self.assertEqual(cs[lower:i], [])
        lower = bisect(0, i, lambda x: lower_predicate(3, x))
        self.assertEqual(cs[lower:i], [])
        lower = bisect(0, i, lambda x: lower_predicate(4, x))
        self.assertEqual(cs[lower:i], [3])
        lower = bisect(0, i, lambda x: lower_predicate(5, x))
        self.assertEqual(cs[lower:i], [4, 3])

    def test_lower_bisect2(self):
        cs = [4, 3, 2, 3, 4]
        i = 2
        ctree = MaxRangeTree(cs)

        def lower_predicate(cap, s):
            return ctree.rmq(s, i + 1) >= cap

        lower = bisect(0, i + 1, lambda x: lower_predicate(1, x))
        self.assertEqual(cs[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(2, x))
        self.assertEqual(cs[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(3, x))
        self.assertEqual(cs[lower:i + 1], [2])
        lower = bisect(0, i + 1, lambda x: lower_predicate(4, x))
        self.assertEqual(cs[lower:i + 1], [3, 2])
        lower = bisect(0, i + 1, lambda x: lower_predicate(5, x))
        self.assertEqual(cs[lower:i + 1], [4, 3, 2])

    def test_lower_bisect3(self):
        cs = [4, 3, 2, 3, 4]
        i = 0
        ctree = MaxRangeTree(cs)

        def lower_predicate(cap, s):
            return ctree.rmq(s, i + 1) >= cap

        lower = bisect(0, i + 1, lambda x: lower_predicate(1, x))
        self.assertEqual(cs[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(2, x))
        self.assertEqual(cs[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(3, x))
        self.assertEqual(cs[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(4, x))
        self.assertEqual(cs[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(5, x))
        self.assertEqual(cs[lower:i + 1], [4])

    def test_lower_bisect4(self):
        cs = [4, 3, 2, 3, 4]
        i = 4
        ctree = MaxRangeTree(cs)

        def lower_predicate(cap, s):
            return ctree.rmq(s, i + 1) >= cap

        lower = bisect(0, i + 1, lambda x: lower_predicate(1, x))
        self.assertEqual(cs[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(2, x))
        self.assertEqual(cs[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(3, x))
        self.assertEqual(cs[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(4, x))
        self.assertEqual(cs[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(5, x))
        self.assertEqual(cs[lower:i + 1], [4, 3, 2, 3, 4])

    def test_lower_bisect5(self):
        cs = [7, 3, 4, 3, 2]
        ds = [5, 4, 3, 2, 1]
        i = 2
        ctree = MaxRangeTree(cs)
        dtree = MaxRangeTree(ds)

        c = cs[i]

        def lower_predicate(cap, s):
            return dtree.rmq(s, i + 1) >= cap or ctree.rmq(s, i + 1) > c

        lower = bisect(0, i + 1, lambda x: lower_predicate(1, x))
        self.assertEqual(ds[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(2, x))
        self.assertEqual(ds[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(3, x))
        self.assertEqual(ds[lower:i + 1], [])
        lower = bisect(0, i + 1, lambda x: lower_predicate(4, x))
        self.assertEqual(ds[lower:i + 1], [3])
        lower = bisect(0, i + 1, lambda x: lower_predicate(5, x))
        self.assertEqual(ds[lower:i + 1], [4, 3])
        lower = bisect(0, i + 1, lambda x: lower_predicate(6, x))
        self.assertEqual(ds[lower:i + 1], [4, 3])

    def test_lower_bisect_6(self):
        cs = [4, 3, 4, 3, 2]
        ds = [5, 4, 3, 2, 1]
        i = 2
        ctree = MaxRangeTree(cs)
        dtree = MaxRangeTree(ds)

        c = cs[i]

        def lower_predicate(cap, s):
            return dtree.rmq(s, i) >= cap or ctree.rmq(s, i) >= c

        lower = bisect(0, i, lambda x: lower_predicate(4, x))
        self.assertEqual(ds[lower:i+1], [3])
        lower = bisect(0, i, lambda x: lower_predicate(5, x))
        self.assertEqual(ds[lower:i+1], [4, 3])
        lower = bisect(0, i, lambda x: lower_predicate(6, x))
        self.assertEqual(ds[lower:i+1], [4, 3])

    def test_lower_bisect_8(self):
        cs = [4, 3, 4, 3, 2]
        ds = [5, 4, 3, 2, 1]
        i = 4
        ctree = MaxRangeTree(cs)
        dtree = MaxRangeTree(ds)

        c = cs[i]

        def lower_predicate(cap, s):
            return dtree.rmq(s, i) >= cap or ctree.rmq(s, i) >= c

        lower = bisect(0, i, lambda x: lower_predicate(4, x))
        self.assertEqual(ds[lower:i+1], [1])
        lower = bisect(0, i, lambda x: lower_predicate(5, x))
        self.assertEqual(ds[lower:i+1], [1])
        lower = bisect(0, i, lambda x: lower_predicate(6, x))
        self.assertEqual(ds[lower:i+1], [1])

    def test_lower_bisect_9(self):
        cs = [4, 3, 4, 3, 2]
        ds = [5, 4, 3, 2, 1]
        i = 0
        ctree = MaxRangeTree(cs)
        dtree = MaxRangeTree(ds)

        c = cs[i]

        def lower_predicate(cap, s):
            return dtree.rmq(s, i) >= cap or ctree.rmq(s, i) >= c

    def test_lower_bisect_10(self):
        cs = [4, 3, 4, 3, 2]
        ds = [5, 4, 3, 2, 1]
        i = 0
        ctree = MaxRangeTree(cs)
        dtree = MaxRangeTree(ds)
        c = cs[i]

        def get_lower(ctree, dtree, i, cap):
            c = ctree.array[i]
            d = dtree.array[i]
            if i == 0:
                return 1 if d >= cap else 0

            def lower_predicate(s):
                return dtree.rmq(s, i) >= cap or ctree.rmq(s, i) >= c
            return bisect(0, i, lower_predicate)

        self.assertEqual(get_lower(ctree, dtree, 0, 4), 1)
        self.assertEqual(get_lower(ctree, dtree, 0, 5), 1)
        self.assertEqual(get_lower(ctree, dtree, 0, 6), 0)

    def test_upper_bisect_1(self):
        cs = [4, 3, 4, 3, 2]
        ds = [1, 2, 3, 4, 5]
        i = 2
        ctree = MaxRangeTree(cs)
        dtree = MaxRangeTree(ds)
        c = cs[i]
        n = len(cs)

        def get_upper(ctree, dtree, i, cap):
            c = ctree.array[i]
            d = dtree.array[i]
            if i + 1 == n:
                return 1 if d >= cap else 0

            def upper_predicate(s):
                return dtree.rmq(i + 1, s + 1) < cap and ctree.rmq(i, s) <= c

            upper = bisect(i + 1, n, upper_predicate)
            return ds[i:upper]

        # self.assertEqual(get_upper(ctree, dtree, i, 3), [3])
        self.assertEqual(get_upper(ctree, dtree, i, 4), [3])
        self.assertEqual(get_upper(ctree, dtree, i, 5), [3, 4])


if __name__ == '__main__':
    main()
