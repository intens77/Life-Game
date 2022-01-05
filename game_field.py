import pygame

from cell import Cell


class GameField(pygame.Surface):
    def __init__(self, width=640, height=480):
        super().__init__((width, height))
        self.__width_in_pixels = width
        self.__height_in_pixels = height
        self.__width_in_cells = width // Cell.size()
        self.__height_in_cells = height // Cell.size()
        self.cells = self.create_cells()

    @property
    def width_in_pixels(self):
        return self.__width_in_pixels

    @property
    def height_in_pixels(self):
        return self.__height_in_pixels

    @property
    def width_in_cells(self):
        return self.__width_in_cells

    @property
    def height_in_cells(self):
        return self.__height_in_cells

    def create_cells(self):
        return [[Cell(x, y) for x in range(self.width_in_cells)] for y in range(self.height_in_cells)]

    def draw_field(self):
        for x in range(0, self.width_in_cells):
            pygame.draw.line(self, pygame.Color('black'), (x, 0), (x, self.get_height()))
        for y in range(0, self.height_in_cells):
            pygame.draw.line(self, pygame.Color('black'), (0, y), (self.get_height(), y))

