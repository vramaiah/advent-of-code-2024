"""Solutions for Day 6"""

from enum import Enum

class GuardDirections(Enum):
    UP = '^'
    DOWN = 'v'
    RIGHT = '>'
    LEFT = '<'


class Map:
    """A class to represent the map of the location, with methods to move the guard"""

    EMPTY = '.'
    OBSTACLE = '#'

    def __init__(self, input_string: str):
        self.map = [list(i) for i in input_string.split('\n')]
        self.guard_dir = GuardDirections.UP
        self.guard_positions = [self.guard_position]


    @property
    def guard_position(self) -> tuple:
        """Returns (row, col) of guard"""
        row_number = None
        for row in self.map:
            if '^' in row or '>' in row or '<' in row or 'v' in row:
                row_number = self.map.index(row)
                break
        return (row_number, self[row_number].index(self.guard_dir.value))

    def __str__(self) -> str:
        return str(self.map)

    def __getitem__(self, index):
        """Index can be in [row] format or (row, column format)"""
        if index is None:
            return None
        if isinstance(index, tuple):
            row, column = index
            return self.map[row][column]
        else:
            return self.map[index]
    
    def __setitem__(self, idx, value):
        row, col = idx
        self.map[row][col] = value
    
    def turn_guard_right(self):
        """Turns the guard right 90 degrees"""
        row, col = self.guard_position
        direction = None
        if self.guard_dir == GuardDirections.UP:
            direction = 90
        elif self.guard_dir == GuardDirections.DOWN:
            direction = 270
        elif self.guard_dir == GuardDirections.RIGHT:
            direction = 0
        elif self.guard_dir == GuardDirections.LEFT:
            direction = 180
        direction -= 90
        if direction == 0:
            self.guard_dir = GuardDirections.RIGHT
        elif direction == 90:
            self.guard_dir = GuardDirections.UP
        elif direction == 180:
            self.guard_dir = GuardDirections.LEFT
        elif direction == 270 or direction == -90:
            self.guard_dir =  GuardDirections.DOWN
        self[row, col] = self.guard_dir.value

    @property
    def square_front_guard_position(self) -> tuple:
        row, column = self.guard_position
        if self.guard_dir == GuardDirections.UP:
            row -= 1
        elif self.guard_dir == GuardDirections.DOWN:
            row += 1
        elif self.guard_dir == GuardDirections.LEFT:
            column -= 1
        elif self.guard_dir == GuardDirections.RIGHT:
            column += 1
        return (row, column)

    @property
    def obstacle_blocking_guard(self):
        # Gets what is in front of the guard
        row, column = self.square_front_guard_position
        item = self[row, column]
        if item == self.OBSTACLE:
            return True
        else:
            return False
    
    def move_guard_foreward(self):
        current_pos = self.guard_position
        new_pos = self.square_front_guard_position
        if not self.obstacle_blocking_guard:
            self[new_pos] = self.guard_dir.value
            self[current_pos] = self.EMPTY
            if not self.guard_position in self.guard_positions:
                self.guard_positions.append(self.guard_position)

    def move(self):
        if not self.obstacle_blocking_guard:
            self.move_guard_foreward()
        else:
            self.turn_guard_right()

    def main(self):
        while True:
            try:
                self.move()
            except IndexError:
                break

def solve_part_1(input_string):
    puzzle_map = Map(input_string)
    puzzle_map.main()
    return len(puzzle_map.guard_positions)

def solve_part_2(input_string: str):
    pass

