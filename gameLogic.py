from dataclasses import dataclass

from Objects.block import Block
from constance import LEVEL_1


@dataclass
class GameLogic:
    logicBoard: list[list[object]]
    objects: list

    def __init__(self):
        self.logicBoard = []
        self.objects = []

    def init_board(self, width: int, height: int):
        self.logicBoard = [[None for _ in range(width)] for _ in range(height)]

    def add_to_logic_board(self, x: int, y: int, obj):
        self.logicBoard[y][x] = obj

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, x: int, y: int):
        self.logicBoard[y][x] = None

    def load_level(self, level: list[list[int]]):
        for y, row in enumerate(level):
            for x, block in enumerate(row):
                if block == 1:  # wall
                    block = Block(x, y, "black")
                    self.add_to_logic_board(x, y, block)
                elif block == 2:  # start
                    block = Block(x, y, "green")
                    self.add_to_logic_board(x, y, block)
                elif block == 3:  # end
                    block = Block(x, y, "red")
                    self.add_to_logic_board(x, y, block)
                else:
                    self.remove_object(x, y)

    def draw_board(self, screen: object):
        for row in self.logicBoard:
            for obj in row:
                if obj is not None:
                    obj.draw(screen=screen)

    def move_objects(self):
        for obj in self.objects:
            obj.move(LEVEL_1)

    def draw_objects(self, screen: object):
        for obj in self.objects:
            obj.draw(screen=screen)
