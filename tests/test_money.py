from tasks.money import Money

def test_money_creation():
    print("Тест 1: Создание объекта Money")
    money = Money(100, 50)
    print("Ожидаем: 100 руб. 50 коп.")
    money.display()

def test_money_addition():
    print("Тест 2: Сложение денежных сумм")
    money1 = Money(100, 50)
    money2 = Money(50, 75)
    result = money1.add(money2)
    print("100.50 + 50.75 = ", end="")
    result.display()
    print("Ожидаем: 151 руб. 25 коп.")

def test_money_subtraction():
    print("Тест 3: Вычитание денежных сумм")
    money1 = Money(100, 50)
    money2 = Money(50, 75)
    result = money1.subtract(money2)
    print("100.50 - 50.75 = ", end="")
    result.display()
    print("Ожидаем: 49 руб. 75 коп.")

def test_money_division():
    print("Тест 4: Деление денежной суммы на число")
    money = Money(100, 50)
    result = money.divide_amount(2)
    print("100.50 / 2 = ", end="")
    result.display()
    print("Ожидаем: 50 руб. 25 коп.")

def test_money_multiplication():
    print("Тест 5: Умножение денежной суммы на число")
    money = Money(100, 50)
    result = money.multiply(1.5)
    print("100.50 * 1.5 = ", end="")
    result.display()
    print("Ожидаем: 150 руб. 75 коп.")

def test_money_comparison():
    print("Тест 6: Сравнение денежных сумм")
    money1 = Money(100, 50)
    money2 = Money(50, 75)
    
    print(f"100.50 == 50.75: {money1.equals(money2)}")
    print(f"100.50 > 50.75: {money1.greater(money2)}")
    print(f"100.50 < 50.75: {money1.less(money2)}")
    print("Ожидаем: False, True, False")

if __name__ == "__main__":
    test_money_creation()
    test_money_addition()
    test_money_subtraction()
    test_money_division()
    test_money_multiplication()
    test_money_comparison()
    print("Все тесты Money завершены!")
