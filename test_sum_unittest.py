import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEquals(sum([1, 2, 3]), 6, "should be 6")

    def test_sum_tuple(self):
        self.assertEquals(sum((1, 2, 2)), 6, "should be 6")


if __name__ == "main":
    unittest.main()
