import pygame
import pygame_widgets
from mybutton import MyButton
from GameWindow import GameWindow

pygame.init()
pygame.font.init()


class Game:
    def __init__(self):
        self.__game_window = GameWindow()
        self.__clock = pygame.time.Clock()
        self.__working_flag = False
        self.__start_flag = False
        self.__game_control_button = MyButton(self.__game_window.window, 600, 200, 100, 50, text='Start',
                                              fontSize=30, inactiveColour=(116, 225, 86),
                                              hoverColour=(49, 117, 31),
                                              pressedColour=(233, 47, 28), onClick=self.handle_control_button_click,
                                              radius=15)
        self.__take_one_step = MyButton(self.__game_window.window, 600, 300, 100, 50, text='One Step',
                                        fontSize=30, inactiveColour=(224, 210, 6),
                                        hoverColour=(106, 100, 17),
                                        pressedColour=(106, 100, 17), onClick=lambda: print('Click'),
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
                        if self.__game_window.check_is_cell(x, y) and not self.__start_flag:
                            cell = self.__game_window.find_clicked_cell(x, y)
                            cell.change_life_state()
            self.__game_window.draw()
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
        else:
            self.__game_control_button.change_text('Start')
            self.__game_control_button.change_states_colors((116, 225, 86), (49, 117, 31), (233, 47, 28))


game = Game()
game.start()
