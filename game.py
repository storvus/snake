import time

import pygame
from pygame.examples.textinput import Screen

from lib.constants import Direction, Color
from lib.coordinates import GameCoordinate
from objects.apple import Apple
from objects.snake import Snake


class Game:

    def __init__(self, screen: Screen) -> None:
        self.screen = screen
        self._is_game_over = False
        self._cooldown = 5
        self.snake = Snake(self)
        self.apple = Apple(self)
        self.apples_eaten = 0

    def handle_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.snake.change_direction(Direction.RIGHT)

        if event.key == pygame.K_LEFT:
            self.snake.change_direction(Direction.LEFT)

        if event.key == pygame.K_UP:
            self.snake.change_direction(Direction.UP)

        if event.key == pygame.K_DOWN:
            self.snake.change_direction(Direction.DOWN)

    @property
    def cooldown(self) -> int:
        return self._cooldown

    def is_apple_point(self, point: GameCoordinate) -> bool:
        apple_coordinates = self.apple.get_coordinates()
        return point.x == apple_coordinates.x and point.y == apple_coordinates.y

    def eat_apple(self):
        self.apple.refresh_coordinates()
        self.apples_eaten += 1
        if self._cooldown < 25:
            self._cooldown += 1

    def get_display_size(self):
        return self.screen.get_size()

    def is_point_inside_field(self, point: GameCoordinate) -> bool:
        width, height = self.get_display_size()
        return 0 <= point.x < width and 0 <= point.y < height

    def show(self):
        self.screen.fill(Color.BLACK)
        self.snake.update()
        self.show_score()
        self.snake.show()
        self.apple.show()

    def get_score(self) -> int:
        return self.apples_eaten

    def is_game_over(self):
        return self._is_game_over

    def game_over(self):
        self._is_game_over = True

    def show_score(self):
        score_font = pygame.font.Font(pygame.font.get_default_font(), 12)
        score_surface = score_font.render(f'Score : {self.apples_eaten}', True, Color.WHITE)
        score_rect = score_surface.get_rect()
        self.screen.blit(score_surface, score_rect)
