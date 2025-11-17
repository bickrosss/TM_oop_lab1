from pair import Pair
from pair import make_pair


def test_pair_creation():
    print("Тест 1: Создание объекта Pair через конструктор")
    pair = Pair(3, 14)
    print("Ожидаем: 3.14")
    pair.display()

def test_make_pair_function():
    print("Тест 2: Создание объекта Pair через функцию make_pair")
    pair = make_pair(2, 5)
    print("Ожидаем: 2.5")
    pair.display()

def test_pair_multiply_positive():
    print("Тест 3: Умножение числа на положительное число")
    pair = Pair(2, 5)
    print("Исходное число: 2.5")
    result = pair.multiply(2)
    print("После умножения на 2:")
    result.display()
    print("Ожидаем: 5.0")

def test_pair_multiply_negative():
    print("Тест 4: Умножение числа на отрицательное число")
    pair = Pair(1, 5)
    print("Исходное число: 1.5")
    result = pair.multiply(-2)
    print("После умножения на -2:")
    result.display()
    print("Ожидаем: -3.0")

def test_pair_multiply_zero():
    print("Тест 5: Умножение числа на ноль")
    pair = Pair(5, 5)
    print("Исходное число: 5.5")
    result = pair.multiply(0)
    print("После умножения на 0:")
    result.display()
    print("Ожидаем: 0.0")


def test_pair_multiply_large():
    print("Тест 6: Умножение числа на большое число")
    pair = Pair(10, 25)
    print("Исходное число: 10.25")
    result = pair.multiply(100)
    print("После умножения на 100:")
    result.display()
    print("Ожидаем: 1025.0")


if __name__ == "__main__":
    test_pair_creation()
    test_make_pair_function()
    test_pair_multiply_positive()
    test_pair_multiply_negative()
    test_pair_multiply_zero()
    test_pair_multiply_large()