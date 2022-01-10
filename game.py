import pygame

from cell import Cell
from game_field import GameField


class Game:
    def __init__(self):
        self.__game_field = GameField()
        self.__clock = pygame.time.Clock()
        self.__working_flag = False

    def start(self):
        pygame.init()
        self.change_working_flag()
        while self.__working_flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.change_working_flag()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cell = self.find_clicked_cell()
                    cell.change_life_state()
                    # clicked_cell = self.find_clicked_cell(pygame.mouse.get_pos())
                    # clicked_cell.change_life_state()
            self.__game_field.draw_field()
            pygame.display.flip()
        pygame.quit()

    def find_clicked_cell(self):
        x, y = pygame.mouse.get_pos()
        row_index, column_index = y // (Cell.size() + self.__game_field.cells_margin), x // (
                    Cell.size() + self.__game_field.cells_margin)
        return self.__game_field.get_cell(row_index, column_index)

    def change_working_flag(self):
        self.__working_flag = not self.__working_flag


game = Game()
game.start()
