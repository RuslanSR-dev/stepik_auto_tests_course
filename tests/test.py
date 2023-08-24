import unittest
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Проверьте, может ли он суммировать список целых чисел
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEquals(result, 6)


if __name__ == "__main__":
    unittest.main()
