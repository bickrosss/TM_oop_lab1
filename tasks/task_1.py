from .pair import Pair
from .pair import make_pair

if __name__ == '__main__':
    print("Создание объектов через конструктор:")
    pair1 = Pair(3, 5)
    pair1.display()
    
    pair2 = Pair(2, 44)
    pair2.display()
    
    print("Создание объектов через функцию make_pair:")
    pair3 = make_pair(7, 8)
    pair3.display()
    
    pair4 = make_pair(4, 20)
    pair4.display()
    
    print("Ввод данных с клавиатуры:")
    pair5 = Pair()
    pair5.read()
    print("Результат ввода:")
    pair5.display()
    
    print("Операция умножения числа на целое число:")
    test_pair = Pair(2, 5)
    print("Исходное число:")
    test_pair.display()
    
    print("Введите целое число для умножения: ")
    multiplier = int(input())
    
    result = test_pair.multiply(multiplier)
    print(f"Результат умножения {test_pair.first}.{test_pair.second} на {multiplier}:")
    result.display()
    
    print("Работа с различными множителями:")
    original_pair = Pair(3, 14)
    
    multipliers = [2, -1, 0, 5]
    for multiplier in multipliers:
        result = original_pair.multiply(multiplier)
        print(f"{original_pair.first}.{original_pair.second} * {multiplier} = ", end="")
        result.display()
    
    print()
    
    print("Демонстрация цепочки операций:")
    start_pair = Pair(1, 5)
    print("Начальное число:")
    start_pair.display()
    
    print("Введите первый множитель: ")
    mult1 = int(input())
    intermediate = start_pair.multiply(mult1)
    print(f"После умножения на {mult1}:")
    intermediate.display()
    
    print("Введите второй множитель: ")
    mult2 = int(input())
    final_result = intermediate.multiply(mult2)
    print(f"После умножения на {mult2}:")
    final_result.display()

