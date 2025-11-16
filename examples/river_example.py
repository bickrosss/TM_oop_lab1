class River:
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)

    def get_info(self):
        print("Длина {0} равна {1} км".format(self.name, self.length))

volga = River("Волга", 3530)
seine = River("Сена", 776)
nile = River("Нил", 6852)

# печатаем все названия рек из атрибута класса
print("Список всех рек:")
for river in River.all_rivers:
    print(river.name)

# вызов метода get_info() разными способами
print("Информация о реках:\n" + "Cпособ 1: self.method()")
volga.get_info()

print("Способ 2: class.method(self)")
River.get_info(volga)
