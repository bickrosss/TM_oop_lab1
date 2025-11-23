from money_package.money import Money

if __name__ == "__main__":
    print("демонстрация работы класса Money:")
    print()
    
    # Создание объектов
    money1 = Money(150, 75)
    money2 = Money(80, 50)
    
    print("Цена1 = ", end="")
    money1.display()
    print("Цена2 = ", end="")
    money2.display()
    print()
    
    # Арифметические операции
    sum_money = money1.add(money2)
    print("Цена1 + Цена2 = ", end="")
    sum_money.display()
    
    diff_money = money1.subtract(money2)
    print("Цена1 - Цена2 = ", end="")
    diff_money.display()
    print()
    
    # Деление и умножение
    divided = money1.divide_amount(3)
    print("Цена1 / 3 = ", end="")
    divided.display()
    
    ratio = money1.divide_by_money(money2)
    print(f"Цена1 / Цена2 = {ratio:.2f}")
    
    multiplied = money2.multiply(1.5)
    print("Цена2 * 1.5 = ", end="")
    multiplied.display()
    print()
    
    # Сравнение
    print(f"money1 == money2: {money1.equals(money2)}")
    print(f"money1 > money2: {money1.greater(money2)}")
    print(f"money1 < money2: {money1.less(money2)}")