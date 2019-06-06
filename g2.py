#
#
#

import sys
import pygame
import time

pygame.init()

WHITE = (255, 255, 255)
GREEN = (27, 127, 66)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)



WINDOWWIDTH = 1920
WINDOWHEIGHT = 1080

WINDOW_SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

#screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

basicFont = pygame.font.SysFont(None,48)
text=basicFont.render("Hello World!", True, WHITE)



## GAME LOOP
while True:
            
            for x in range(0,255):
                        COLOR = (x,0,0)
                        print (COLOR)
            WINDOW_SURFACE.fill(COLOR)
            
            textRect = text.get_rect()
            textRect.centerx = WINDOW_SURFACE.get_rect().centerx
            textRect.centery = WINDOW_SURFACE.get_rect().centery
            WINDOW_SURFACE.blit(text, textRect)
            
            pygame.display.update()
            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit(0)
            
