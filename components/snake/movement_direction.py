from typing import Tuple

from lib.constants import Direction
from lib.coordinates import GameCoordinate


class MovementDirection:

    forbidden_turns = {
        Direction.LEFT: [Direction.RIGHT],
        Direction.RIGHT: [Direction.LEFT],
        Direction.UP: [Direction.DOWN],
        Direction.DOWN: [Direction.UP],
    }

    def __init__(self, step_size) -> None:
        self.step_size = step_size
        self.current_direction = None
        self.next_direction = self.current_direction
        self.update_direction(Direction.RIGHT)

    def get_next_coordinates_for_point(self, point: GameCoordinate) -> GameCoordinate:
        if self.next_direction in self.forbidden_turns.get(self.current_direction, []):
            print(f"Cannot change the direction to the opposite. Current direction: {self.current_direction}. "
                  f"Requested direction: {self.next_direction}")
            self.next_direction = self.current_direction
            return self._get_next_coordinates_for_point(point)
        self.current_direction = self.next_direction
        return self._get_next_coordinates_for_point(point)

    def update_direction(self, next_direction: Direction):
        self.next_direction = next_direction

    def _get_next_coordinates_for_point(self, point: GameCoordinate) -> GameCoordinate:
        shift_x, shift_y = 0, 0
        if self.current_direction == Direction.RIGHT:
            shift_x, shift_y = self.step_size, 0
        if self.current_direction == Direction.LEFT:
            shift_x, shift_y = -1 * self.step_size, 0
        if self.current_direction == Direction.UP:
            shift_x, shift_y = 0, -1 * self.step_size
        if self.current_direction == Direction.DOWN:
            shift_x, shift_y = 0, self.step_size
        return GameCoordinate(x=point.x + shift_x, y=point.y + shift_y)
