import pygame

from game_field import GameField


class Game:
    def __init__(self):
        self.__game_window = GameField()
        self.screen = pygame.display.set_mode((self.__game_window.width_in_pixels, self.__game_window.height_in_pixels))

    def start(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.__game_window.fill(pygame.Color('black'))
        running = True
        while running:
            self.__game_window.draw_field()
            pygame.display.flip()
        pygame.quit()


game = Game()
game.start()
