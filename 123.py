import unittest
from lab1 import pythonlab1 as main
class TestfindInd2(unittest.TestCase):

    def test_basic_case(self):#Тест базовый
        self.assertEqual(main.findInd2([1, 2, 3, 4], 5), (0, 3))  # 1 + 4 = 5

    def test_no_pair_found(self):#Тест без подходящей пары
        self.assertEqual(main.findInd2([1, 2, 3, 4], 10), 0)

    def test_negative_numbers(self):#Тест с отрицательными числами и положительной суммой
        self.assertEqual(main.findInd2([-1, 2, -3, 4], 1), (0, 1))  # -1 + 4 = 3

    def test_zero_target(self):#Тест с нулевой искомой суммой
        self.assertEqual(main.findInd2([1, -1, 2, 3], 0), (0, 1))  # 1 + (-1) = 0

    def test_empty_list(self):#Тест с пустым масивом на ввод
        self.assertEqual(main.findInd2([], 5), 0)

    def test_string_in_list(self):#Тест с одним String
        self.assertFalse(main.findInd2([1, 'a', 3, 4], 5))

    def test_float_in_list(self):#Тест с float
        self.assertFalse(main.findInd2([1, 2.5, 3, 4], 5))

    def test_none_in_list(self):#Тест с None
        self.assertFalse(main.findInd2([1, None, 3, 4], 5))

    def test_large_numbers(self):#Тест с большими числами
        self.assertEqual(main.findInd2([1000000, 2000000, 3000000], 5000000), (1, 2))  # 1M + 4M = 5M

    def test_multiple_pairs(self): #Тест с несколькими подходящими парами
        self.assertEqual(main.findInd2([1, 4, 2, 3, 1], 5), (0, 1))  # 1 + 4 = 5 (первая найденная)

    def test_identical_numbers(self):#Тест с одинаковыми элементами в масиве
        self.assertEqual(main.findInd2([5, 5, 5, 5], 10), (0, 1))  # 5 + 5 = 10

    def test_zero_in_list(self):#Тест с нулем в масиве
        self.assertEqual(main.findInd2([0, 1, 2, 3], 3), (0, 3))  # 0 + 3 = 3

    def test_negative_target(self):#Тест с отрицательной суммой
        self.assertEqual(main.findInd2([1, -2, 3, -4], -6), (1, 3))  # -2 + (-4) = -6

    def test_large_list(self):#Тест с большим масивом
        large_list = list(range(100))
        self.assertEqual(main.findInd2(large_list, 197), (98, 99))

    def test_no_duplicate_indices(self): #Тест на одинаковые индексы
        result = main.findInd2([5, 10, 15], 10)
        # Не должно вернуть (0, 0) или (1, 1) и т.д.
        self.assertNotEqual(result, (0, 0))
        self.assertNotEqual(result, (1, 1))
        self.assertNotEqual(result, (2, 2))

    def test_mixed_invalid_types(self): #Тест со смешанными невалидными типами
        self.assertFalse(main.findInd2([1, [2, 3], 'text', 4], 5))

    def test_all_strings(self): #Проверка со всеми переменными типа String
        self.assertFalse(main.findInd2(['1', '2', '3'], 3))

    def test_boolean_values(self): # Проверка с булевыми переменными в масиве
        self.assertFalse(main.findInd2([True, False, 1, 2], 2))


if __name__ == '__main__':
    unittest.main()
