import unittest
from complex_number import ComplexNumber, find_largest_magnitude, print_summary

class TestComplexNumber(unittest.TestCase):
    # Набор тестов для проверки работы класса ComplexNumber

    def test_addition(self):
        # Тест сложения двух комплексных чисел
        num1 = ComplexNumber(3, 4)
        num2 = ComplexNumber(1, -2)
        result = num1 + num2
        self.assertEqual(result.real, 4)      # Проверяем действительную часть
        self.assertEqual(result.imaginary, 2)  # Проверяем мнимую часть

    def test_subtraction(self):
        # Тест вычитания двух комплексных чисел
        num1 = ComplexNumber(3, 4)
        num2 = ComplexNumber(1, -2)
        result = num1 - num2
        self.assertEqual(result.real, 2)
        self.assertEqual(result.imaginary, 6)

    def test_multiplication(self):
        # Тест умножения двух комплексных чисел
        num1 = ComplexNumber(3, 4)
        num2 = ComplexNumber(1, -2)
        result = num1 * num2
        self.assertEqual(result.real, 11)
        self.assertEqual(result.imaginary, -2)

    def test_magnitude(self):
        # Тест вычисления модуля числа (3 + 4i) → √(3²+4²) = 5
        num = ComplexNumber(3, 4)
        self.assertAlmostEqual(num.magnitude(), 5.0)

    def test_str_representation(self):
        # Тест строкового представления числа с отрицательной мнимой частью
        num = ComplexNumber(3, -4)
        self.assertEqual(str(num), "3 - 4i")

    def test_find_largest_magnitude_normal(self):
        # Тест поиска числа с наибольшим модулем в обычном списке
        numbers = [ComplexNumber(1, 1), ComplexNumber(3, 4), ComplexNumber(0, 1)]
        largest = find_largest_magnitude(numbers)
        self.assertEqual(largest.real, 3)
        self.assertEqual(largest.imaginary, 4)

    def test_find_largest_magnitude_empty(self):
        # Тест для пустого списка — должен вернуть None
        self.assertIsNone(find_largest_magnitude([]))

    def test_type_error_addition(self):
        # Тест на ошибку при попытке сложить число с некомплексным объектом
        num = ComplexNumber(1, 1)
        with self.assertRaises(TypeError):
            num + "invalid"

if __name__ == '__main__':
    unittest.main()
