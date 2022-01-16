import pygame

from model.cell import Cell


class GameField:
    def __init__(self, width=545, height=545):
        self.__window = pygame.Surface((width, height))
        self.__width_in_pixels = width
        self.__height_in_pixels = height
        self.__cells_margin = 5

        self.__width_in_cells = width // Cell.size()
        self.__height_in_cells = height // Cell.size()
        self.__cells = self.create_cells()

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

    @property
    def cells_margin(self):
        return self.__cells_margin

    @property
    def surface(self):
        return self.__window

    @property
    def cells(self):
        return self.__cells

    def create_cells(self):
        return [[Cell(x, y) for x in range(0, self.width_in_pixels, Cell.size())]
                for y in range(0, self.height_in_pixels, Cell.size())]

    @property
    def window(self):
        return self.__window

    def get_cell(self, row_index, column_index):
        return self.__cells[row_index][column_index]

    def find_clicked_cell(self, x, y):
        row_index, column_index = y // (Cell.size() + self.cells_margin), x // (
                Cell.size() + self.cells_margin)
        return self.get_cell(row_index, column_index)

    def set_cells(self, new_cells):
        self.__cells = new_cells
