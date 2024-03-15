from abc import ABC
from dataclasses import dataclass
import pygame
import constance


@dataclass
class Block:
    x: int
    y: int
    color: str
    width: int = constance.BLOCK_SIZE

    def __init__(self, x: int, y: int, color: str):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color,
                         (self.x * self.width, self.y * self.width, self.width, self.width))  # draw the block
        pygame.draw.rect(screen, "white",
                         (self.x * self.width, self.y * self.width, self.width, self.width),
                         1)  # draw the border

    def click(self):
        ...

    def move(self, target_x: int, target_y: int):
        ...
