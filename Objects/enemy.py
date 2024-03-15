from abc import ABC
from dataclasses import dataclass
from constance import BLOCK_SIZE
import pygame


def find_target(level: list[list[int]]) -> tuple[int, int]:
    for y, row in enumerate(level):
        for x, block in enumerate(row):
            if block == 3:
                return x, y
    return -1, -1


def check_collision(x, y, level):
    return level[y][x] == 1


@dataclass
class Enemy:
    x: int
    y: int
    color: str
    health: int
    speed: int
    direction: tuple[int, int]
    been: set[tuple[int, int]]

    def __init__(self, x: int, y: int, color: str):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.health = 100
        self.direction = (1, 1)
        self.been = set()
        self.alive = True

    def draw(self, screen: object):
        radius = BLOCK_SIZE // 4
        # draw the circle in the center of the block
        pygame.draw.circle(screen, self.color,
                           (self.x * BLOCK_SIZE + BLOCK_SIZE // 2, self.y * BLOCK_SIZE + BLOCK_SIZE // 2),
                           radius)

        # draw the border
        pygame.draw.circle(screen, "white",
                           (self.x * BLOCK_SIZE + BLOCK_SIZE // 2, self.y * BLOCK_SIZE + BLOCK_SIZE // 2),
                           radius, 1)

        # draw the health bar
        pygame.draw.rect(screen, "red", (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE , BLOCK_SIZE, 5))

        pygame.draw.rect(screen, "green", (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE , BLOCK_SIZE * (self.health / 100), 5))

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        print("Enemy died")
        self.x = -1
        self.y = -1
        self.alive = False


    def move(self, level: list[list[int]]):

        self.been.add((self.x, self.y))

        target = find_target(level)
        if target == (-1, -1):
            return

        target_x, target_y = target

        if self.x == target_x and self.y == target_y:
            self.die()
            return

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            new_x = self.x + direction[0]
            new_y = self.y + direction[1]
            if (new_x, new_y) not in self.been and not check_collision(new_x, new_y, level):
                self.been.add((new_x, new_y))
                self.x = new_x
                self.y = new_y
                return








