from threading import Timer

import pygame
import pygame_widgets

from button import MyButton
from game_field import GameField

pygame.init()
pygame.font.init()


class Game:
    def __init__(self, width=750, height=545):
        self.__window = pygame.display.set_mode((width, height))
        self.__window.fill(pygame.Color('black'))
        pygame.display.set_caption('Game of Life')
        self.__width = width
        self.__height = height
        self.__game_field = GameField()
        self.__clock = pygame.time.Clock()
        self.__working_flag = False
        self.__start_flag = False
        self.__timer = None
        self.__game_control_button = MyButton(self.__window, 600, 200, 100, 50, text='Start',
                                              fontSize=30, inactiveColour=(116, 225, 86),
                                              hoverColour=(49, 117, 31),
                                              pressedColour=(233, 47, 28), onClick=self.handle_control_button_click,
                                              radius=15)
        self.__take_one_step = MyButton(self.__window, 600, 300, 100, 50, text='One Step',
                                        fontSize=30, inactiveColour=(224, 210, 6),
                                        hoverColour=(106, 100, 17),
                                        pressedColour=(106, 100, 17), onClick=self.step,
                                        radius=15)

    def start(self):
        self.change_working_flag()
        while self.__working_flag:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.change_working_flag()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        if self.check_is_cell(x, y) and not self.__start_flag:
                            cell = self.find_clicked_cell(x, y)
                            cell.change_life_state()
            self.draw_game_window()
            pygame_widgets.update(events)
            pygame.display.update()
        pygame.quit()

    def change_working_flag(self):
        self.__working_flag = not self.__working_flag

    def change_start_flag(self):
        self.__start_flag = not self.__start_flag

    def handle_control_button_click(self):
        self.change_start_flag()
        if self.__start_flag:
            self.__game_control_button.change_text('Stop')
            self.__game_control_button.change_states_colors((233, 47, 28), (154, 32, 19), (116, 225, 86))
            self.__timer = self.create_timer()
            self.__timer.start()
        else:
            self.__game_control_button.change_text('Start')
            self.__game_control_button.change_states_colors((116, 225, 86), (49, 117, 31), (233, 47, 28))
            self.__timer.cancel()
            print('thats all')

    def create_timer(self, function=None, interval=0.05):
        function = self.play if function is None else function
        return Timer(interval, function)

    def play(self):
        self.__timer = self.create_timer()
        self.step()
        self.__timer.start()

    def step(self):
        print('HI')
        # new_cells = self.__game_field.create_cells()
        # for row in self.__game_field.cells:
        #     for cell in row:

    def draw_game_window(self):
        self.__game_field.draw()
        self.__window.blit(self.__game_field.surface, (0, 0))

    def find_clicked_cell(self, x, y):
        return self.__game_field.find_clicked_cell(x, y)

    def check_is_cell(self, x, y):
        return x < self.__game_field.width_in_pixels and y < self.__game_field.height_in_pixels


game = Game()
game.start()
