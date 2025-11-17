from pair import Pair, make_pair

if __name__ == "__main__":
    print("Индивидуальное задание 1")
    print("Класс Pair с методами multiply")
    print()
    
    # Демонстрация создания объектов
    print("Создание объектов Pair:")
    pair1 = Pair(3.14, 5)
    pair1.display()
    
    pair2 = make_pair(2.5, 8)
    pair2.display()
    print()
    
    # Демонстрация ввода с клавиатуры
    print("Ввод данных с клавиатуры:")
    pair3 = Pair()
    pair3.read()
    print("Результат ввода:")
    pair3.display()
    print()
    
    # Демонстрация метода multiply
    print("Демонстрация метода multiply:")
    
    print("Умножение на положительное число:")
    result1 = pair1.multiply(3)
    result1.display()
    
    print("Умножение на отрицательное число:")
    result2 = pair2.multiply(-2)
    result2.display()
    
    print("Умножение на ноль:")
    result3 = pair1.multiply(0)
    result3.display()
    print()
    
    # Демонстрация работы с разными значениями
    print("Работа с разными значениями:")
    pairs = [
        Pair(1.5, 2),
        Pair(0.0, 0),
        Pair(-2.7, 3),
        Pair(10.2, 15)
    ]
    
    for i, pair in enumerate(pairs, 1):
        print(f"Пара {i}: ", end="")
        pair.display()
        multiplied = pair.multiply(2)
        print(f"  Умноженная на 2: ", end="")
        multiplied.display()
