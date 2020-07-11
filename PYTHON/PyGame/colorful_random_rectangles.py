import pygame
pygame.init()
import random
screen = pygame.display.set_mode((1000,700))


while (True):
    x = random.randrange(0, 1000)
    y = random.randrange(0, 700)
    width = random.randrange(0, 1000)
    height = random.randrange(0, 700)
    R = random.randrange(0, 256)
    G = random.randrange(0, 256)
    B = random.randrange(0, 256)
    pygame.draw.rect(screen, (R,G,B), [x,y,height,width], 1)
    pygame.display.update()
