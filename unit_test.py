# unit_test.py

import unittest
from choice_sort import Sorter

class TestSort(unittest.TestCase):
    def test_sort(self):
        sorter = Sorter()

        sorter.log = self.mock_log

        # Тест на пустом массиве
        self.assertEqual(sorter.sort([]), [])
        
        # Тест на массиве из одного элемента
        self.assertEqual(sorter.sort([22]), [22])
        
        # Тест на массиве из нескольких элементов
        self.assertEqual(sorter.sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
        
        # Тест на массиве с отрицательными числами
        self.assertEqual(sorter.sort([-5, -1, -3, -2, -4]), [-5, -4, -3, -2, -1])
        
        # Тест на массиве с повторяющимися элементами
        self.assertEqual(sorter.sort([5, 3, 5, 2, 8, 2]), [2, 2, 3, 5, 5, 8])
        
        # Тест на уже отсортированном массиве
        self.assertEqual(sorter.sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        
        # Тест на массиве, отсортированном в обратном порядке
        self.assertEqual(sorter.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def mock_log(self, *text):
        print(*text)