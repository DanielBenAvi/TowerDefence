from dataclasses import dataclass

import pygame

from Objects.bullet import Bullet
from Objects.enemy import Enemy
from constance import BLOCK_SIZE


@dataclass
class Tower:
    x: int
    y: int
    color: str
    damage: int
    range: int

    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y
        self.color = "blue"
        self.range = 3
        self.damage = 10
        self.bullets = []

    def draw(self, screen: object):
        # draw the small square in the center of the block
        pygame.draw.rect(screen, self.color,
                         (self.x * BLOCK_SIZE + BLOCK_SIZE // 3, self.y * BLOCK_SIZE + BLOCK_SIZE // 3,
                          BLOCK_SIZE // 3, BLOCK_SIZE // 3))

    def attack(self, enemy: Enemy):
        if inRange(self.x, self.y, enemy.x, enemy.y, self.range):
            bullet = Bullet(self.x, self.y, enemy.x, enemy.y, enemy)
            self.bullets.append(bullet)


def inRange(x1, y1, x2, y2, rad):
    return abs(x1 - x2) <= rad and abs(y1 - y2) <= rad
