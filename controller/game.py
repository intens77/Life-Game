from threading import Timer

import pygame

from model.button import MyButton
from model.game_field import GameField
from view import viever

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
                                        pressedColour=(106, 100, 17), onClick=self.take_one_step,
                                        radius=15)

        self.__clear_field_button = MyButton(self.__window, 600, 400, 100, 50, text='Clear',
                                             fontSize=30, inactiveColour=(72, 66, 76),
                                             hoverColour=(36, 31, 40),
                                             pressedColour=(72, 66, 76), onClick=self.clearn_button_click_handler,
                                             radius=15)

    @property
    def game_field(self):
        return self.__game_field

    @property
    def window(self):
        return self.__window

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
            viever.update_game_state(self, events)
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

    def create_timer(self, function=None, interval=0.05):
        function = self.play if function is None else function
        return Timer(interval, function)

    def play(self):
        self.__timer = self.create_timer()
        self.take_one_step()
        self.__timer.start()

    def compare_game_states(self, new_cells):
        for x in range(self.__game_field.width_in_cells):
            for y in range(self.__game_field.height_in_cells):
                if self.__game_field.get_cell(y, x).life_state != new_cells[y][x].life_state:
                    return False
        return True

    def clearn_button_click_handler(self):
        if not self.__start_flag:
            for x in range(self.__game_field.width_in_cells):
                for y in range(self.__game_field.height_in_cells):
                    self.__game_field.get_cell(y, x).life_state = False

    def take_one_step(self):
        new_cells = self.__game_field.create_cells()
        self.__game_field.create_cells()
        for x in range(self.__game_field.width_in_cells):
            for y in range(self.__game_field.height_in_cells):
                alive_neighbours_count = self.get_alive_neighbours_count(x, y)
                cell = self.game_field.get_cell(y, x)
                if cell.life_state and (alive_neighbours_count == 2 or alive_neighbours_count == 3):
                    new_cells[y][x].change_life_state()
                if not cell.life_state and alive_neighbours_count == 3:
                    new_cells[y][x].change_life_state()
        if self.compare_game_states(new_cells):
            self.handle_control_button_click()
        self.__game_field.set_cells(new_cells)

    def get_alive_neighbours_count(self, x, y):
        alive_neighbours_count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dx == dy:
                    continue
                neighbour = self.__game_field.get_cell((y + dy) % self.__game_field.height_in_cells,
                                                       (x + dx) % self.__game_field.width_in_cells)
                if neighbour.life_state:
                    alive_neighbours_count += 1
        return alive_neighbours_count

    def find_clicked_cell(self, x, y):
        return self.__game_field.find_clicked_cell(x, y)

    def check_is_cell(self, x, y):
        return x < self.__game_field.width_in_pixels and y < self.__game_field.height_in_pixels
