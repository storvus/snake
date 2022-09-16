import random

import pygame

from lib.constants import Color
from lib.coordinates import GameCoordinate


class Apple:
    apple_size = 10

    def __init__(self, game) -> None:
        self.game = game
        self.refresh_coordinates()

    def get_coordinates(self):
        return self.coordinates

    def refresh_coordinates(self):
        width, height = self.game.get_display_size()
        coords_x = random.randrange(0, width, 10)
        coords_y = random.randrange(0, height, 10)
        self.coordinates = GameCoordinate(x=coords_x, y=coords_y)

    def show(self):
        rect = pygame.Rect(self.coordinates.x, self.coordinates.y, self.apple_size, self.apple_size)
        pygame.draw.rect(self.game.screen, Color.RED, rect)
