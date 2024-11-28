from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=True):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(*new_color):
        check = True
        for color in new_color:
            if color < 0 or color > 255:
                check = False
        return check

    def set_color(self, *new_color):
        if Figure.__is_valid_color(*new_color):
            self.__color = new_color

    def __is_valid_sides(self, *new_sides):
        check = True
        for sides in new_sides:
            if sides < 0 and type(sides) is not int:
                check = False
        return check

    def get_sides(self):
        return self.__sides

    def __len__(self):
        if self.sides_count == 1:
            return self.__sides[0]
        elif self.sides_count == 3 or self.sides_count == 12:
            return len(range(sum(self.__sides)))
        else:
            return 'Ошибка!!!'

    def set_sides(self, *new_sides):
        if len(list(new_sides)) == self.sides_count and Figure.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled=True):
        self.sides = list(sides)
        if len(self.sides) == self.sides_count:
            self.sides = self.sides_count * self.sides
        else:
            self.sides = self.sides_count * [1]

        self.radius = self.sides[0] / 2 * pi
        super().__init__(color, self.sides, filled)

    def get_square(self):
        S = pi * self.radius ** 2
        return S


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled=True):
        if len(list(sides)) == self.sides_count:
            self.sides = list(sides)
        else:
            self.sides = 3 * [1]

        super().__init__(color, self.sides, filled)

    def get_square(self):
        p = 0.5 * sum(self.sides)
        S = sqrt(p * (p - self.sides[1]) * (p - self.sides[2]) * (p - self.sides[3]))
        return S


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled=True):
        self.sides = list(sides)
        if len(list(sides)) == 1:
            self.sides = self.sides_count * self.sides
        else:
            self.sides = self.sides_count * [1]

        super().__init__(color, self.sides, filled)

    def get_volume(self):
        volume = self.sides[1] ** 3
        return volume


cirlce1 = Circle((200, 100, 100), 10)
cube1 = Cube((222, 35, 130), 6)

cirlce1.set_color(55, 66, 77)
print(cirlce1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
cirlce1.set_sides(15)
print(cirlce1.get_sides())

print(len(cirlce1))

print(cube1.get_volume())