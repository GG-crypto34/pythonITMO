import unittest

from lab2 import lab2.py as main
class testGuessNumber(unittest.TestCase):
    def test_1(self):#проверка на количесво сравнений
        self.assertEqual(main.guess_number(target=5, ranges=(0,10), mode="binary"), (1,5))
    def test_2(self):#проверка на количесво сравнений
        self.assertEqual(main.guess_number(target=5, ranges=(0, 10), mode="seq"), (6,5))
    def test_3(self):#проверка на отсутсвие числа в промежутке
        self.assertEqual(main.guess_number(target=15, ranges=(0,10), mode="binary"), (-1,15))
    def test_4(self):#проверка на отсутсвие числа в промежутке
        self.assertEqual(main.guess_number(target=15, ranges=(0, 10), mode="seq"), (-1,15))
    def test_7(self):#проверка на ошибку типа данных
        with self.assertRaises(TypeError):
            main.guess_number(target=5, ranges=(0, 10), mode="ABCD")
    def test_8(self):#проверка на ошибку типа данных
        with self.assertRaises(TypeError):
            main.guess_number(target='A', ranges=(0, 10), mode="seq")
    def test_9(self):#проверка на ошибку типа данных
        with self.assertRaises(TypeError):
            main.guess_number(target=5, ranges=('0', 10), mode="seq")
