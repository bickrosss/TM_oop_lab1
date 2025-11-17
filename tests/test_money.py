from money_package.money import Money

def test_money_creation():
    money = Money(100, 50)
    assert money.rubles == 100
    assert money.kopecks == 50

def test_money_addition():
    m1 = Money(100, 50)
    m2 = Money(50, 75)
    result = m1.add(m2)
    assert result.rubles == 151
    assert result.kopecks == 25

def test_money_subtraction():
    m1 = Money(100, 50)
    m2 = Money(50, 75)
    result = m1.subtract(m2)
    assert result.rubles == 49
    assert result.kopecks == 75

def test_money_comparison():
    m1 = Money(100, 50)
    m2 = Money(50, 75)
    assert m1.greater(m2) == True
    assert m2.less(m1) == True
