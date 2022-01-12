import pygame

from game_field import GameField


class GameWindow:
    def __init__(self, width=750, height=545):
        self.__window = pygame.display.set_mode((width, height))
        self.__window.fill(pygame.Color('black'))
        pygame.display.set_caption('Game of Life')
        self.__width = width
        self.__height = height
        self.__game_field = GameField()

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def window(self):
        return self.__window

    def draw(self):
        self.__game_field.draw()
        self.__window.blit(self.__game_field.surface, (0, 0))

    def find_clicked_cell(self, x, y):
        return self.__game_field.find_clicked_cell(x, y)

    def check_is_cell(self, x, y):
        return x < self.__game_field.width_in_pixels and y < self.__game_field.height_in_pixels
