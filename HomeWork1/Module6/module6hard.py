import math as m

class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = self.__is_filled()

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = self.__is_filled()

    def __is_filled(self):
        return self.__color != [0, 0, 0]

    def __is_valid_sides(self, *sides):
        return all(isinstance(s, int) and s > 0 for s in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(1)
        self.__radius = self.get_sides()[0] / (2 * m.pi)

    def __radius(self):
        return self.__radius

    def get_square(self):
        return m.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(*([1] * self.sides_count))
        self.__height = self.__calculate_height()

    def get_height(self):
        return self.__height

    def __calculate_height(self):
        first, second, third = self.get_sides()
        half_of_per = sum([first, second, third]) / 2
        area = m.sqrt(half_of_per * (half_of_per - first) * (half_of_per - second) * (half_of_per - third))
        return 2 * area / first

    def get_square(self):
        first, _, _ = self.get_sides()
        return 0.5 * first * self.__height

class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(*([1] * self.sides_count))

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
