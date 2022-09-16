import sys, pygame
import time

from game import Game
from lib.constants import Color

pygame.init()
pygame.display.set_caption('Snake')
width, height = 320, 440
screen = pygame.display.set_mode([width, height])
fps = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 36)

game = Game(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            game.handle_keyup(event)

        if event.type == pygame.QUIT:
            sys.exit()
    if game.is_game_over():
        game_over_surface = font.render(f'Your Score is : {game.get_score()}', True, Color.RED)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (width / 2, height / 4)
        screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

    game.show()
    pygame.display.update()
    fps.tick(game.cooldown)
