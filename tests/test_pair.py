from pair import Pair


def test_pair_creation():
    pair = Pair(3.14, 5)
    assert pair.first == 3.14
    assert pair.second == 5
    print("тест пройден")


def test_pair_multiply():
    pair = Pair(2.5, 4)
    result = pair.multiply(3)
    assert result.first == 7.5
    assert result.second == 12
    print("тест пройден")


def test_pair_multiply_negative():
    pair = Pair(1.5, 3)
    result = pair.multiply(-2)
    assert result.first == -3.0
    assert result.second == -6
    print("тест пройден")


def test_pair_multiply_zero():
    pair = Pair(4.2, 7)
    result = pair.multiply(0)
    assert result.first == 0.0
    assert result.second == 0
    print("тест пройден")


def test_make_pair():
    pair = make_pair(1.1, 2)
    assert pair.first == 1.1
    assert pair.second == 2
    print("тест пройден")


if __name__ == "__main__":
    test_pair_creation()
    test_pair_multiply()
    test_pair_multiply_negative()
    test_pair_multiply_zero()
    test_make_pair()
    print("Все тесты пройдены!")
