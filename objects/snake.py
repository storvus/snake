import pygame

from components.snake.movement_direction import MovementDirection
from lib.constants import Direction, Color
from lib.coordinates import GameCoordinate


class Snake:
    element_size = 10

    def __init__(self, game) -> None:
        self.game = game
        self.direction = Direction.RIGHT
        self.movement_direction = MovementDirection(self.element_size)
        self.body = [
            GameCoordinate(x=0, y=0),
            GameCoordinate(x=10, y=0),
            GameCoordinate(x=20, y=0),
            GameCoordinate(x=30, y=0),
            GameCoordinate(x=40, y=0),
        ]

    def change_direction(self, new_direction: Direction):
        self.movement_direction.update_direction(new_direction)

    def move(self):
        head_position = self.body[-1]
        head_new_position = self.movement_direction.get_next_coordinates_for_point(head_position)
        if not self.game.is_point_inside_field(head_new_position):
            self.game.game_over()
        if head_new_position in self.body:
            self.game.game_over()
        if self.game.is_apple_point(head_new_position):
            self.game.eat_apple()
        else:
            self.body.pop(0)
        self.body.append(GameCoordinate(x=head_new_position.x, y=head_new_position.y))

    def update(self):
        self.move()

    def show(self):
        for el in self.body:
            rect = pygame.Rect(el.x, el.y, self.element_size, self.element_size)
            pygame.draw.rect(self.game.screen, Color.WHITE, rect)
