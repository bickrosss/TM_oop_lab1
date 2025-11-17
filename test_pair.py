from pair import Pair, make_pair


def test_pair_creation():
    print("Тест создания пары:")
    pair = Pair(3.14, 5)
    pair.display()
    print()


def test_make_pair():
    print("Тест функции make_pair:")
    pair = make_pair(2.5, 8)
    pair.display()
    print()


def test_pair_multiply():
    print("Тест умножения пары:")
    pair = Pair(2.0, 3)
    result = pair.multiply(4)
    print("Исходная пара:")
    pair.display()
    print("После умножения на 4:")
    result.display()
    print()


if __name__ == "__main__":
    test_pair_creation()
    test_make_pair()
    test_pair_multiply()
    
    print("Все тесты завершены!")