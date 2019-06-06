#
#
#

import sys
import pygame

pygame.init()

WHITE = (255, 255, 255)
GREEN = (27, 127, 66)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)



WINDOWWIDTH = 1920
WINDOWHEIGHT = 1080

WINDOW_SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

basicFont = pygame.font.SysFont(None,48)
text=basicFont.render("Hello World!", True, WHITE)


## GAME LOOP
while True:
            WINDOW_SURFACE.fill(BLACK)
            
            pygame.draw.line(WINDOW_SURFACE, GREEN, (500,800), (490, 860), 10)      #b
            pygame.draw.line(WINDOW_SURFACE, GREEN, (490,860), (490, 1080), 5)      #l1
            pygame.draw.line(WINDOW_SURFACE, GREEN, (500,800), (470, 860), 10)      #l2
            pygame.draw.line(WINDOW_SURFACE, GREEN, (500,800), (470, 860), 10)      #a1
            pygame.draw.line(WINDOW_SURFACE, GREEN, (500,800), (470, 860), 10)      #a
            
            pygame.draw.circle(WINDOW_SURFACE, WHITE, (500, 800), 20)
            
            #pygame.draw.ellipse(WINDOW_SURFACE, BLUE, (100, 200, 300, 400))
            pygame.draw.rect(WINDOW_SURFACE, BLUE, (0,920,1920,1080))
            textRect = text.get_rect()
            textRect.centerx = WINDOW_SURFACE.get_rect().centerx
            textRect.centery = WINDOW_SURFACE.get_rect().centery
            WINDOW_SURFACE.blit(text, textRect)
            
            pygame.display.update()
            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit(0)
            
