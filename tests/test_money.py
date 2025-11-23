from money_package.money import Money

def test_money_creation():
    """Тест создания объекта Money"""
    money = Money(100, 50)
    assert money.rubles == 100
    assert money.kopecks == 50

def test_money_addition():
    """Тест сложения денежных сумм"""
    m1 = Money(100, 50)
    m2 = Money(50, 75)
    result = m1.add(m2)
    assert result.rubles == 151
    assert result.kopecks == 25

def test_money_subtraction():
    """Тест вычитания денежных сумм"""
    m1 = Money(100, 50)
    m2 = Money(50, 75)
    result = m1.subtract(m2)
    assert result.rubles == 49
    assert result.kopecks == 75

def test_money_comparison():
    """Тест сравнения денежных сумм"""
    m1 = Money(100, 50)
    m2 = Money(50, 75)
    assert m1.greater(m2) == True
    assert m2.less(m1) == True
    assert m1.equals(m1) == True

def test_money_division():
    """Тест деления денежной суммы"""
    m1 = Money(300, 0)
    result = m1.divide_amount(3)
    assert result.rubles == 100
    assert result.kopecks == 0

def test_money_multiplication():
    """Тест умножения денежной суммы"""
    m1 = Money(100, 50)
    result = m1.multiply(2)
    assert result.rubles == 201
    assert result.kopecks == 0
    