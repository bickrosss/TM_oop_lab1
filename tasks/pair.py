class Pair:
    def __init__(self, first=0.0, second=0):
        self.first = float(first)
        self.second = int(second)

    def read(self):
        self.first = float(input("Введите first (вещественное число): "))
        self.second = int(input("Введите second (положительное целое): "))

    def display(self):
        print(f"Pair: first = {self.first}, second = {self.second}")

    def multiply(self, number):
        new_first = self.first * number
        new_second = self.second * number
        return Pair(new_first, new_second)


def make_pair(first, second):
    return Pair(first, second)


if __name__ == "__main__":
    print("Демонстрация класса Pair")
    
    # Создание через конструктор
    pair1 = Pair(3.14, 5)
    print("pair1:", end=" ")
    pair1.display()
    
    # Создание через make_pair
    pair2 = make_pair(2.5, 8)
    print("pair2:", end=" ")
    pair2.display()
    
    # Ввод с клавиатуры
    print("Введите данные для pair3:")
    pair3 = Pair()
    pair3.read()
    print("pair3:", end=" ")
    pair3.display()
    
    # Умножение
    result = pair1.multiply(3)
    print("pair1 * 3:", end=" ")
    result.display()
    
    # Умножение отрицательного числа
    result2 = pair2.multiply(-2)
    print("pair2 * (-2):", end=" ")
    result2.display()
    
    # Умножение на ноль
    result3 = pair1.multiply(0)
    print("pair1 * 0:", end=" ")
    result3.display()
