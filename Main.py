import pygame, sys
from settings import *
from Logic import Game

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Mini Golf")
clock = pygame.time.Clock()

main = Game(screen=screen)

while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main.run()

    pygame.display.flip()
    clock.tick(60)