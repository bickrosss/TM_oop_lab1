#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import gcd as gsd


class Pair:
    def __init__(self, first=0, second=0):
        if not isinstance(first, (int, float)):
            print("Ошибка: first должно быть числом")
            exit(1)
        if not isinstance(second, int) or second < 0:
            print("Ошибка: second должно быть положительным целым числом")
            exit(1)
        
        self.first = int(first)
        self.second = int(second)

    def read(self):
        try:
            self.first = int(input("Введите целую часть числа: "))
            second_input = int(input("Введите дробную часть числа: "))
            if second_input < 0:
                print("Ошибка: дробная часть должна быть положительной")
                exit(1)
            self.second = second_input
        except ValueError:
            print("Ошибка: введите целые числа")
            exit(1)

    def display(self):
        print(f"Число: {self.first}.{self.second}")

    def multiply(self, number):
        if not isinstance(number, int):
            print("Ошибка: множитель должен быть целым числом")
            exit(1)
            
        full_number = float(f"{self.first}.{self.second}")
        result_number = full_number * number
        result_str = str(result_number)
        parts = result_str.split('.')
        new_first = int(parts[0])
        new_second = int(parts[1]) if len(parts) > 1 else 0
        result_pair = Pair(new_first, new_second)
        return result_pair


def make_pair(first, second):
    if not isinstance(first, (int, float)):
        print("Ошибка: first должно быть числом")
        exit(1)
    if not isinstance(second, int) or second < 0:
        print("Ошибка: second должно быть положительным целым числом")
        exit(1)
    
    return Pair(first, second)