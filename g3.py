#
#
#

import sys
import pygame
import time
import math

pygame.init()

WHITE = (255, 255, 255)
GREEN = (27, 127, 66)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

backBarColor = (0, 104, 127)
backBarColor1 = (11, 71, 74)
frontBarColor = (127, 17, 22)
groundColor = (0, 127, 34)

clock = pygame.time.Clock()

WINDOWWIDTH = 1920
WINDOWHEIGHT = 1080

WINDOW_SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

rectangle = pygame.Rect(0,0,60,60)

powerBarRect = pygame.Rect(40, 20, 500, 50)
powerBarRectSlider = pygame.Rect(45, 27, 50, 30)
powerBarRectBack = pygame.Rect(35, 15, 510, 60)
groundRect = pygame.Rect(0, 520, 1900, 700)


##ERROR
basicFont = pygame.font.SysFont(None, 50)


speed = 1
alpha = 0
gravity = 9.81
tick = 0


## GAME LOOP
while True:
            WINDOW_SURFACE.fill(WHITE)
            
            
            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit(0)
            
                        if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                                pygame.quit()
                                                sys.exit(0)

                                    if event.key == pygame.K_LEFT and powerBarRectSlider.left != 45:
                                                powerBarRectSlider.left -= 10
                                                pygame.event.post(event)
                                                
                                    if event.key == pygame.K_RIGHT and powerBarRectSlider.left <= 480:
                                                powerBarRectSlider.left += 10
                                                pygame.event.post(event)

                                    if event.key == pygame.K_UP and alpha > -90:
                                                alpha-=1
                                                pygame.event.post(event)
                                    if event.key == pygame.K_DOWN and alpha != 0:
                                                alpha+=1
                                                pygame.event.post(event)

                        if event.type == pygame.KEYUP:
                                    pygame.event.clear()
                                    
            #Error
            #powerText = basicFont.render("Power:")                      
            length = 400
            lStart = (30, 500)
            lEnd = (lStart[0]+length*math.cos(math.radians(alpha)), lStart[1]+length*math.sin(math.radians(alpha)))
            pygame.draw.line(WINDOW_SURFACE, BLACK, lStart, lEnd, 2)
            pygame.draw.circle(WINDOW_SURFACE, GREEN, lStart, 25)
            pygame.draw.rect(WINDOW_SURFACE, backBarColor1, powerBarRectBack)
            pygame.draw.rect(WINDOW_SURFACE, backBarColor, powerBarRect)
            pygame.draw.rect(WINDOW_SURFACE, groundColor, groundRect)
            
            pygame.draw.rect(WINDOW_SURFACE, WHITE, powerBarRectSlider)

            
            pygame.display.update()
            clock.tick(30)
                        
            
