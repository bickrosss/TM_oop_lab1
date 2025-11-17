from pair import Pair
from pair import make_pair

if __name__ == '__main__':
    print("Демонстрация создания объектов через конструктор:")
    print("Создаем число 3.5")
    pair1 = Pair(3, 5)
    pair1.display()
    
    print("Создаем число 2.44")
    pair2 = Pair(2, 44)
    pair2.display()
    
    print("Демонстрация создания объектов через функцию make_pair:")
    print("Создаем число 7.8 с помощью make_pair(7, 8)")
    pair3 = make_pair(7, 8)
    pair3.display()
    
    print("Создаем число 4.20 с помощью make_pair(4, 20)")
    pair4 = make_pair(4, 20)
    pair4.display()
    
    print("Демонстрация ввода данных с клавиатуры:")
    print("Создаем пустое число и заполняем его через метод read()")
    pair5 = Pair()
    pair5.read()
    print("Результат ввода:")
    pair5.display()
    
    print("Демонстрация операции умножения числа на целое число:")
    test_pair = Pair(2, 5)
    print("Исходное число:")
    test_pair.display()
    
    print("Умножаем число 2.5 на 3:")
    multiplied1 = test_pair.multiply(3)
    multiplied1.display()
    
    print("Умножаем число 2.5 на 2:")
    multiplied2 = test_pair.multiply(2)
    multiplied2.display()
    
    print("Умножаем число 2.5 на 10:")
    multiplied3 = test_pair.multiply(10)
    multiplied3.display()
    
    print("Демонстрация цепочки операций:")
    print("Создаем число 1.5, умножаем на 3, затем на 2:")
    chain_result = Pair(1, 5)
    print("Исходное число:")
    chain_result.display()
    intermediate_result = chain_result.multiply(3)
    print("После умножения на 3:")
    intermediate_result.display()
    final_result = intermediate_result.multiply(2)
    print("После умножения на 2:")
    final_result.display()
    print()
    
    print("Дополнительные примеры работы с различными значениями:")
    example_pairs = [
        Pair(0, 0),
        Pair(1, 1),
        Pair(3, 75),
        Pair(10, 99)
    ]
    
    for i, pair in enumerate(example_pairs, 1):
        print(f"Пример {i}:")
        pair.display()
        multiplied = pair.multiply(2)
        print(f"После умножения на 2:")
        multiplied.display()
        print()
