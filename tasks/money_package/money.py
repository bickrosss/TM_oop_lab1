class Money:
    def __init__(self, rubles=0, kopecks=0):
        self.rubles = rubles
        self.kopecks = kopecks
        self._normalize()

    def _normalize(self):
        if self.kopecks >= 100:
            self.rubles += self.kopecks // 100
            self.kopecks = self.kopecks % 100
        elif self.kopecks < 0:
            self.rubles -= (-self.kopecks) // 100 + 1
            self.kopecks = 100 - ((-self.kopecks) % 100)

    def read(self):
        self.rubles = int(input("Введите рубли: "))
        self.kopecks = int(input("Введите копейки: "))
        self._normalize()

    def display(self):
        print(f"{self.rubles} руб. {self.kopecks:02d} коп.")

    def add(self, other):
        new_rubles = self.rubles + other.rubles
        new_kopecks = self.kopecks + other.kopecks
        return Money(new_rubles, new_kopecks)

    def subtract(self, other):
        new_rubles = self.rubles - other.rubles
        new_kopecks = self.kopecks - other.kopecks
        return Money(new_rubles, new_kopecks)

    def divide_amount(self, n):
        total_kopecks = self.rubles * 100 + self.kopecks
        result_kopecks = total_kopecks // n
        return Money(0, result_kopecks)

    def divide_by_money(self, other):
        total_kopecks1 = self.rubles * 100 + self.kopecks
        total_kopecks2 = other.rubles * 100 + other.kopecks
        return total_kopecks1 / total_kopecks2

    def multiply(self, factor):
        total_kopecks = self.rubles * 100 + self.kopecks
        result_kopecks = int(total_kopecks * factor)
        return Money(0, result_kopecks)

    def equals(self, other):
        return (self.rubles == other.rubles) and (self.kopecks == other.kopecks)

    def greater(self, other):
        total1 = self.rubles * 100 + self.kopecks
        total2 = other.rubles * 100 + other.kopecks
        return total1 > total2

    def less(self, other):
        total1 = self.rubles * 100 + self.kopecks
        total2 = other.rubles * 100 + other.kopecks
        return total1 < total2
