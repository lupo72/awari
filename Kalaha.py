# -*- coding: utf-8 -*-
import re
import pygame
pygame.init()
SCREENDIM = (640,480)
screen = pygame.display.set_mode(SCREENDIM)
hg = pygame.Surface(SCREENDIM)
hg.fill( (0,0,0) )
screen.blit( hg, (0,0) )
font = pygame.font.Font(None, 24)

class Kalaha(pygame.sprite.Sprite):

    def __init__(self):
        pass

    def draw_board(self):
        pass




loop = True

while loop == True:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                pass
            elif e.key == pygame.K_RIGHT:
                pass
            elif e.key == pygame.K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
        elif e.type == pygame.QUIT:
            pygame.quit()


    output = font.render( "Screenoutput",1 , (255,255,255), (0,0,0) )

    screen.blit(output,(0,0))

    pygame.display.flip()
