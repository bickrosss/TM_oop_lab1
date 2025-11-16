class Rectangle1:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, w):
        self._width = w

    def get_height(self):
        return self._height

    def set_height(self, h):
        self._height = h

    def area(self):
        return self._width * self._height


print("работа с защищенными атрибутами:")
rect1 = Rectangle1(10, 20)
print(f"через getter: {rect1.get_width()}")
print(f"прямой доступ: {rect1._width}")
print(f"площадь: {rect1.area()}")

print("изменение защищенных атрибутов:")
rect1.set_width(15)
print(f"через setter: {rect1.get_width()}")
rect1._width = 25
print(f"прямое изменение: {rect1._width}")
print()


class Rectangle2:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, w):
        self.__width = w

    def get_height(self):
        return self.__height

    def set_height(self, h):
        self.__height = h

    def area(self):
        return self.__width * self.__height


print("работа с приватными атрибутами:")
rect2 = Rectangle2(30, 40)
print(f"через getter: {rect2.get_width()}")
print(f"площадь: {rect2.area()}")

print(f"{rect2._Rectangle2__width}")
rect2._Rectangle2__width = 35
print(f"после изменения: {rect2.get_width()}")
print()


class Rectangle3:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError

    def area(self):
        return self.__width * self.__height


print("работа со свойствами")
rect3 = Rectangle3(50, 60)
print(rect3.width)
print(rect3.height)
print(rect3.area())

print("изменение свойств:")
rect3.width = 55
rect3.height = 65
print(rect3.width)
print(rect3.height)
print(rect3.area())