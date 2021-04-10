import pygame
from pygame.locals import *
import sys

print('shark longer')
pygame.init()
screen = pygame.display.set_mode((500, 500))
myfont = pygame.font.Font(None, 50)
white = 255, 255, 255
blue = 0, 255, 255
textImage = myfont.render("FUCK", True, white)
screen.fill(blue)
screen.blit(textImage, (100, 100))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
