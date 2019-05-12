"""
Utility functions to copy/paste around to quickly get the min of a large set
of ranges. Should be O(n) to construct, O(log n) to find.
"""
from unittest import TestCase, main


class RangeTree:
    def __init__(self, array, start=None, end=None):
        self.array = array
        assert array, 'Array must be non-empty'
        self.start = 0 if start == None else start
        self.end = len(array) if end == None else end
        self.set_tree()

    def set_tree(self):
        if self.start == self.end - 1:
            self.value = self.array[self.start]
        else:
            midpoint = (self.start + self.end) // 2
            self.left = self.__class__(self.array, self.start, midpoint)
            self.right = self.__class__(self.array, midpoint, self.end)
            self.value = self.compare(self.left.value, self.right.value)

    def rmq(self, start, end):
        assert start < end, '{} >= {}'.format(start, end)
        if self.start == start and self.end == end:
            return self.value

        if start >= self.right.start:
            return self.right.rmq(start, end)

        if end <= self.left.end:
            return self.left.rmq(start, end)

        return self.compare(
            self.left.rmq(start, self.left.end),
            self.right.rmq(self.right.start, end)
        )


class MinRangeTree(RangeTree):
    compare = min


class MaxRangeTree(RangeTree):
    compare = max


def bisect(start, end, lambda_):
    """
    Assuming that it exists, this function returns x in start <= x <= end s.t
    all([lambda[i] for i in range(start, x)]) == True
    any([lambda[i] for i in range(x, end)]) == False
    """
    assert start < end, '{} >= {}'.format(start, end)
    if start == end - 1:
        return end if lambda_(start) else start

    midpoint = (start + end) // 2
    if lambda_(midpoint):
        return bisect(midpoint, end, lambda_)
    else:
        return bisect(start, midpoint, lambda_)

#
### Tests ###
#


class TestNode(TestCase):
    def test_builds_smallest_tree(self):
        node = MinRangeTree([0], 0, 1)
        self.assertEqual(node.value, 0)
        self.assertFalse(hasattr(node, 'left'))
        self.assertFalse(hasattr(node, 'right'))

    def test_builds_second_smallest_tree(self):
        node = MinRangeTree([0, 1], 0, 2)
        self.assertEqual(node.value, 0)
        self.assertEqual(node.left.value, 0)
        self.assertEqual(node.right.value, 1)
        self.assertFalse(hasattr(node.left, 'left'))
        self.assertFalse(hasattr(node.left, 'right'))
        self.assertFalse(hasattr(node.right, 'left'))
        self.assertFalse(hasattr(node.right, 'right'))

    def test_find_min_on_exact_match(self):
        tree = MinRangeTree([0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(tree.rmq(0, 7), 0)

    def test_find_min_on_nested_exact_match(self):
        tree = MinRangeTree([0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(tree.rmq(3, 5), 3)

    def test_find_min_on_non_exact_match(self):
        tree = MinRangeTree([6, 5, 4, 3, 2, 1, 0])
        self.assertEqual(tree.rmq(0, 6), 1)
        self.assertEqual(tree.rmq(1, 7), 0)
        self.assertEqual(tree.rmq(1, 6), 1)

    def test_well_formed_arrays(self):
        with self.assertRaises(AssertionError):
            MinRangeTree([])

    def test_well_formed_queries(self):
        tree = MinRangeTree([0, 1, 2])
        with self.assertRaises(AssertionError):
            tree.rmq(0, 0)
        with self.assertRaises(AssertionError):
            tree.rmq(2, 1)

    def test_max_range_tree(self):
        tree = MaxRangeTree([6, 5, 4, 3, 2, 1, 0])
        self.assertEqual(tree.rmq(0, 6), 6)
        self.assertEqual(tree.rmq(1, 7), 5)
        self.assertEqual(tree.rmq(1, 6), 5)


class TestBisect(TestCase):
    def test_all_true(self):
        def predicate(_):
            return True
        self.assertEqual(bisect(0, 10, predicate), 10)
        self.assertTrue(all(predicate(i) for i in range(0, 10)))
        self.assertFalse(any(predicate(i) for i in range(10, 10)))

    def test_all_false(self):
        def predicate(_):
            return False
        self.assertEqual(bisect(0, 10, predicate), 0)
        self.assertTrue(all(predicate(i) for i in range(0, 0)))
        self.assertFalse(any(predicate(i) for i in range(0, 10)))

    def test_first_five_true(self):
        def predicate(i):
            return i < 5
        self.assertEqual(bisect(0, 10, predicate), 5)
        self.assertTrue(all(predicate(i) for i in range(0, 5)))
        self.assertFalse(any(predicate(i) for i in range(5, 10)))

    def test_bad_input(self):
        with self.assertRaises(AssertionError):
            bisect(0, 0, lambda _: False)
        with self.assertRaises(AssertionError):
            bisect(2, 0, lambda _: False)


if __name__ == '__main__':
    main()
