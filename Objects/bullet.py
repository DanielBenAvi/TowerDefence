from dataclasses import dataclass

import pygame

from Objects.enemy import Enemy
from constance import BLOCK_SIZE


def check_collision(x, y, obj):
    return pygame.Rect(x, y, 1, 1).colliderect(obj)


@dataclass
class Bullet:
    x_current: float
    y_current: float
    x_target: float
    y_target: float
    x_start: float
    y_start: float
    target = None
    alive: bool = True

    def __init__(self, x_start: float, y_start: float, x_target: float, y_target: float, target: Enemy):
        self.x_current = x_start
        self.y_current = y_start
        self.x_start = x_start
        self.y_start = y_start
        self.x_target = x_target
        self.y_target = y_target
        self.target = target

    def draw(self, screen: pygame.Surface):
        # pygame.draw.circle(screen, "red",
        #                    (self.x_current*BLOCK_SIZE + BLOCK_SIZE//2, self.y_current*BLOCK_SIZE + BLOCK_SIZE//2),
        #                    2)

        pygame.draw.line(screen, "red",
                         (self.x_start * BLOCK_SIZE + BLOCK_SIZE // 2, self.y_start * BLOCK_SIZE + BLOCK_SIZE // 2),
                         (self.x_target * BLOCK_SIZE + BLOCK_SIZE // 2, self.y_target * BLOCK_SIZE + BLOCK_SIZE // 2))

    def move(self):
        if self.x_current == self.x_target and self.y_current == self.y_target:
            self.alive = False
            self.target.take_damage(10)


        if self.x_current < self.x_target:
            self.x_current += 1
        elif self.x_current > self.x_target:
            self.x_current -= 1

        if self.y_current < self.y_target:
            self.y_current += 1
        elif self.y_current > self.y_target:
            self.y_current -= 1
