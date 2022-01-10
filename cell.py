import pygame


class Cell:
    __size = 40

    def __init__(self, x, y, life_state=False):
        self.__x = x
        self.__y = y
        self.__life_state = life_state

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

    def change_life_state(self):
        self.__life_state = not self.__life_state

    def draw(self, screen, horizontal_margin, vertical_margin):
        color = pygame.Color('green') if self.__life_state else pygame.Color('white')
        pygame.draw.rect(screen, color,
                         (self.x + horizontal_margin, self.y + vertical_margin, self.size(), self.size()))
