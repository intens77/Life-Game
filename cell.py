class Cell:
    __size = 10

    def __init__(self, x, y, visibility=False):
        self.__x = x
        self.__y = y
        self.__visibility = visibility

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @classmethod
    def size(cls):
        return cls.__size

    def change_visibility(self):
        self.__visibility = not self.__visibility
