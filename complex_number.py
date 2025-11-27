import math

class ComplexNumber:
    # Класс для работы с комплексными числами (вида a + bi)

    def __init__(self, real, imaginary):
        # Задаём действительную и мнимую части числа
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        # Сложение двух комплексных чисел
        # Проверяем, что второй операнд — тоже комплексное число
        if not isinstance(other, ComplexNumber):
            raise TypeError("Можно складывать только комплексные числа")
        # Складываем действительные и мнимые части по отдельности
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        # Вычитание двух комплексных чисел
        # Проверяем тип второго операнда
        if not isinstance(other, ComplexNumber):
            raise TypeError("Можно вычитать только комплексные числа")
        # Вычитаем действительные и мнимые части
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        # Умножение двух комплексных чисел по формуле:
        # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        if not isinstance(other, ComplexNumber):
            raise TypeError("Можно умножать только комплексные числа")
        # Вычисляем действительную часть (ac - bd)
        real_part = self.real * other.real - self.imaginary * other.imaginary
        # Вычисляем мнимую часть (ad + bc)
        imaginary_part = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        # Преобразуем комплексное число в строку вида "a ± bi"
        # Определяем знак перед мнимой частью
        sign = '+' if self.imaginary >= 0 else '-'
        # Возвращаем строку, используя модуль мнимой части
        return f"{self.real} {sign} {abs(self.imaginary)}i"

    def magnitude(self):
        # Вычисляем модуль (длину вектора) комплексного числа
        # Формула: √(a² + b²)
        return math.sqrt(self.real**2 + self.imaginary**2)


def find_largest_magnitude(numbers_list):
    # Находим число с наибольшим модулем в списке
    # Если список пуст — возвращаем None
    if not numbers_list:
        return None

    # Берём первое число как начальное максимальное
    largest = numbers_list[0]
    # Проходим по всем числам в списке
    for num in numbers_list:
        # Если текущее число больше максимального — обновляем максимум
        if num.magnitude() > largest.magnitude():
            largest = num
    return largest


def print_summary(real_part, imag_part):
    # Печатаем отдельно действительную и мнимую части числа
    print(f"Действительная часть: {real_part}, Мнимая часть: {imag_part}")

# Пример использования класса
num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, -2)
num3 = ComplexNumber(0, 5)

print("Число 1:", num1)
print("Число 2:", num2)
print("Сложение:", num1 + num2)
print("Вычитание:", num1 - num2)
print("Умножение:", num1 * num2)
print("Модуль числа 1:", num1.magnitude())

numbers = [num1, num2, num3]
largest_num = find_largest_magnitude(numbers)
print("Число с наибольшим модулем:", largest_num)

print_summary(10, 20)