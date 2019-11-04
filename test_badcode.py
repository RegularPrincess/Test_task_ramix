import unittest
from badcode import good_funny_function,is_increase_for_1


class TestGoodFunnyFunction(unittest.TestCase):
    def setUp(self):
        self.data_same1 = [1, 1, 1, 1]
        self.data_same2 = ['a', 'a', 'a', 'a']
        self.data_not_same1 = [1, 1, 1, 1, 2]

        self.data_increase1 = [1, 2, 3, 4]
        self.data_increase2 = ['1', '2', '3', '4']
        self.data_increase3 = [1, 2, 3, '4']

        self.data_decrease1 = [3, 2, 1, 0]
        self.data_decrease2 = [3, 2, '1', 0]
        self.data_decrease3 = ['3', '2', '1', '0']

        self.data_too_short = []
        self.data_type_error = [1, '2', 'jk', 3]
        self.data_none = None

    def test_all_same_int(self):
        self.assertEqual(good_funny_function(self.data_same1), 1)

    def test_all_same_str(self):
        self.assertEqual(good_funny_function(self.data_same2), 1)

    def test_not_same_int(self):
        self.assertEqual(good_funny_function(self.data_not_same1), None)

    def test_increase_1(self):
        self.assertEqual(good_funny_function(self.data_increase1), 1)

    def test_increase_2(self):
        self.assertEqual(good_funny_function(self.data_increase2), 1)

    def test_increase_3(self):
        self.assertEqual(good_funny_function(self.data_increase3), 1)

    def test_decrease_1(self):
        self.assertEqual(good_funny_function(self.data_decrease1), 1)

    def test_decrease_2(self):
        self.assertEqual(good_funny_function(self.data_decrease2), 1)

    def test_decrease_3(self):
        self.assertEqual(good_funny_function(self.data_decrease3), 1)

    def test_data_none(self):
        with self.assertRaises(ValueError):
            good_funny_function(self.data_none)

    def test_data_too_short(self):
        with self.assertRaises(ValueError):
            good_funny_function(self.data_too_short)

    def test_data_error(self):
        self.assertEqual(good_funny_function(self.data_type_error), None)


class TestIsIncrease(unittest.TestCase):
    def setUp(self):
        self.data_increase1 = [1, 2, 3, 4]
        self.data_increase2 = ['1', '2', '3', '4']
        self.data_increase3 = [1, 2, 3, '4']

        self.data_type_error = [1, '2', 'jk', 3]

    def test_increase_int(self):
        self.assertEqual(is_increase_for_1(self.data_increase1), True)

    def test_increase_str(self):
        self.assertEqual(is_increase_for_1(self.data_increase2), True)

    def test_increase_mix(self):
        self.assertEqual(is_increase_for_1(self.data_increase3), True)

    def test_data_error(self):
        self.assertEqual(is_increase_for_1(self.data_type_error), False)


if __name__ == '__main__':
    unittest.main()
