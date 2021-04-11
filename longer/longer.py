import pygame
from pygame.locals import *
import sys

print('shark longer')
pygame.init()

if not pygame.font.get_init():
    pygame.font.init()

screen = pygame.display.set_mode((500, 500))
myfont = pygame.font.Font(None, 100)
white = 255, 255, 255
red = 255, 0, 0
textImage = myfont.render("STOP", True, white)
screen.fill(red)
screen.blit(textImage, (170, 200))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
print("shayu")
