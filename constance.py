import pygame

'''
Game CONSTANTS
'''
FPS: int = 60
WINDOW_WIDTH: int = 1280  # 16:9 aspect ratio
WINDOW_HEIGHT: int = WINDOW_WIDTH // 16 * 9  # 16:9 aspect ratio
BLOCK_SIZE: int = 40  # size of each block in the grid
GRID_WIDTH: int = WINDOW_WIDTH // BLOCK_SIZE  # number of blocks wide
GRID_HEIGHT: int = WINDOW_HEIGHT // BLOCK_SIZE  # number of blocks tall

'''
Pygame CONSTANTS
'''
CLOCK = pygame.time.Clock()
MOVE_OBJECTS = pygame.USEREVENT + 1
CREATE_ENEMY = pygame.USEREVENT + 2

'''
Level CONSTANTS
'''

# Level 1
LEVEL_1: list[list[int]] = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 3],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
