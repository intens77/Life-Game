import pygame
import pygame_widgets


def update_game_state(game, events):
    draw_game_field(game.game_field)
    game.window.blit(game.game_field.surface, (0, 0))
    pygame_widgets.update(events)
    pygame.display.update()


def draw_game_field(game_field):
    for row_index in range(game_field.height_in_cells):
        for column_index in range(game_field.width_in_cells):
            cell = game_field.get_cell(row_index, column_index)
            draw_cell(cell, game_field.window, (column_index + 1) * game_field.cells_margin,
                      (row_index + 1) * game_field.cells_margin)


def draw_cell(cell, screen, horizontal_margin, vertical_margin):
    color = pygame.Color('green') if cell.life_state else pygame.Color('white')
    pygame.draw.rect(screen, color,
                     (cell.x + horizontal_margin, cell.y + vertical_margin, cell.size(), cell.size()))
