#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pair import Pair
from pair import make_pair


if __name__ == "__main__":
    print("=== Демонстрация класса Pair ===")
    
    print("1. Создание через конструктор:")
    pair1 = Pair(3, 5)
    pair1.display()
    
    pair2 = Pair(2, 44)
    pair2.display()
    
    print("2. Создание через make_pair:")
    pair3 = make_pair(7, 8)
    pair3.display()
    
    pair4 = make_pair(4, 20)
    pair4.display()
    
    print("3. Ввод с клавиатуры:")
    pair5 = Pair()
    pair5.read()
    pair5.display()
    
    print("4. Умножение на произвольное целое число:")
    test_pair = Pair(2, 5)
    test_pair.display()
    
    try:
        multiplier = int(input("Введите целое число для умножения: "))
        result = test_pair.multiply(multiplier)
        print(f"Результат умножения: ", end="")
        result.display()
    except ValueError:
        print("Ошибка: введите целое число")
        exit(1)
    
    print("5. Демонстрация работы с разными множителями:")
    original_pair = Pair(3, 14)
    
    multipliers = [2, -1, 0, 5]
    for multiplier in multipliers:
        result = original_pair.multiply(multiplier)
        print(f"{original_pair.first}.{original_pair.second} * {multiplier} = ", end="")
        result.display()
    
    print("6. Цепочка операций:")
    start_pair = Pair(1, 5)
    print("Начальное число: ", end="")
    start_pair.display()
    
    try:
        mult1 = int(input("Введите первый множитель: "))
        intermediate = start_pair.multiply(mult1)
        print("После первого умножения: ", end="")
        intermediate.display()
        
        mult2 = int(input("Введите второй множитель: "))
        final_result = intermediate.multiply(mult2)
        print("После второго умножения: ", end="")
        final_result.display()
    except ValueError:
        print("Ошибка: введите целые числа")
        exit(1)