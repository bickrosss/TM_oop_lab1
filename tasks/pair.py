class Pair:
    def __init__(self, first=0.0, second=0):
        self.first = int(first)
        self.second = int(second)

    def read(self):
        print("Введите целую часть числа (first): ")
        first_value = input()
        self.first = int(first_value)
        
        print("Введите дробную часть числа (second): ")
        second_value = input()
        self.second = int(second_value)

    def display(self):
        print(f"Число: {self.first}.{self.second}")

    def multiply(self, number):
        full_number = float(f"{self.first}.{self.second}")
        result_number = full_number * number
        result_str = str(result_number)
        parts = result_str.split('.')
        new_first = int(parts[0])
        new_second = int(parts[1]) if len(parts) > 1 else 0
        result_pair = Pair(new_first, new_second)
        return result_pair


def make_pair(first, second):
    new_pair = Pair(first, second)
    return new_pair
