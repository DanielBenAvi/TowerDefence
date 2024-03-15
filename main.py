import pygame

from Objects.block import Block
from Objects.enemy import Enemy
from Objects.tower import Tower
from constance import FPS, WINDOW_WIDTH, WINDOW_HEIGHT, CLOCK, GRID_WIDTH, GRID_HEIGHT, LEVEL_1, BLOCK_SIZE, \
    MOVE_OBJECTS, CREATE_ENEMY, TOWER_ATTACK, BULLET_MOVE
from gameLogic import GameLogic

pygame.init()
pygame.time.set_timer(MOVE_OBJECTS, 1000)
pygame.time.set_timer(CREATE_ENEMY, 2000)
pygame.time.set_timer(TOWER_ATTACK, 200)
pygame.time.set_timer(BULLET_MOVE, 50)

pygame.display.set_caption("Tower Defense")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

game = GameLogic()
game.init_board(GRID_WIDTH, GRID_HEIGHT)
game.load_level(LEVEL_1)


def click() -> tuple[int, int]:
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0] // BLOCK_SIZE
    y = mouse_pos[1] // BLOCK_SIZE
    return x, y


def main():
    # pygame setup
    running = True

    while running:
        game.remove_dead()
        pygame.display.set_caption(f"Tower Defense - Points: {game.points}")

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = click()
                print(x, y)
                for obj in game.enemies:
                    if isinstance(obj, Enemy):
                        if obj.x == x and obj.y == y:
                            obj.take_damage(10)

                if isinstance(game.logicBoard[y][x], Block):
                    print("clicked on block")
                    game.logicBoard[y][x].click()
                    game.add_tower(Tower(x, y))

            if event.type == MOVE_OBJECTS:
                game.move_objects()

            if event.type == CREATE_ENEMY:
                game.add_enemy(Enemy(0, 1, "white"))

            if event.type == TOWER_ATTACK:
                for obj in game.towers:
                    if len(game.enemies) > 0:
                        obj.attack(game.enemies[0])

            if event.type == BULLET_MOVE:
                game.move_bullets()
                ...

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE
        game.draw_board(screen)
        game.draw_objects(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        CLOCK.tick(FPS)  # limits FPS to 60

    pygame.quit()


if __name__ == '__main__':
    main()
