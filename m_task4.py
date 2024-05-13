import numpy as np


class GeometricObject:

    def __init__(self, x: float = 0.0, y: float = 0.0, color: str = 'black', filled: bool = False):
        self.__x = float(x)
        self.__y = float(y)
        self.color = color
        self.filled = filled

    def __repr__(self):
        if self.filled:
            text = 'filled'
        else:
            text = 'no filled'
        return f'({int(self.__x)}, {int(self.__y)}) {self.color} {text}'

    def __str__(self):
        return f'({self.__x}, {self.__y})\ncolor: {self.color}\nfilled: {self.filled}'

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_color(self):
        return self.color

    def is_filled(self):
        return self.filled

    def set_coordinate(self, x: float, y: float):
        self.__x = float(x)
        self.__y = float(y)

    def set_color(self, color: str):
        self.color = color

    def set_filled(self, filled: bool):
        self.filled = filled


class Circle(GeometricObject):

    def __init__(self, x: float = 0.0, y: float = 0.0, r: float = 0.0, color: str = 'black', filled: bool = False):
        super().__init__(x=x, y=y, color=color, filled=filled)
        self.__x = float(x)
        self.__y = float(y)
        if r < 0:
            self.__radius = 0.0
        else:
            self.__radius = float(r)

    def __repr__(self):
        if self.filled:
            text = 'filled'
        else:
            text = 'no filled'
        return f'radius: {int(self.__radius)} ({int(self.get_x())}, {int(self.get_y())}) {self.color} {text}'

    def __str__(self):
        return f'radius: {self.__radius}\n({self.get_x()}, {self.get_y()})\ncolor: {self.color}\nfilled: {self.filled}'

    @property
    def radius(self):
        return self.__radius

    @radius.getter
    def radius(self):
        if self.__radius < 0:
            return 0.0
        return float(self.__radius)

    @radius.setter
    def radius(self, r: float):
        if r < 0:
            self.__radius = 0.0
        else:
            self.__radius = float(r)

    def get_area(self):
        return np.pi * self.radius ** 2

    def get_perimetr(self):
        return 2 * np.pi * self.radius

    def get_diametr(self):
        return 2 * self.radius


class Rectangle(GeometricObject):

    def __init__(self, x: float = 0.0, y: float = 0.0, width: float = 0.0, height: float = 0.0, color: str = 'black',
                 filled: bool = False):
        super().__init__(x=x, y=y, color=color, filled=filled)
        self.__x = x
        self.__y = y

        if width < 0:
            self.width = 0.0
        else:
            self.width = float(width)

        if height < 0:
            self.height = 0.0
        else:
            self.height = float(height)

    def __repr__(self):
        if self.filled:
            text = 'filled'
        else:
            text = 'no filled'
        return (f'width: {int(self.width)} height: {int(self.height)} ({int(self.get_x())}, {int(self.get_y())})'
                f' {self.color} {text}')

    def __str__(self):
        return (f'width: {self.width}\nheight: {self.height}\n({self.get_x()}, {self.get_y()})\ncolor: '
                f'{self.color}\nfilled: {self.filled}')

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimetr(self):
        return 2 * (self.width + self.height)

    def set_width(self, width: float):
        if width < 0:
            self.width = 0.0
        else:
            self.width = float(width)

    def set_height(self, height: float):
        if height < 0:
            self.height = 0.0
        else:
            self.height = float(height)
