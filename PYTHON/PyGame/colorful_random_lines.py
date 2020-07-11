import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1000,700))

while (True):
    x1 = random.randrange(0, 1000)
    x2 = random.randrange(0, 1000)
    y1 = random.randrange(0, 700)
    y2 = random.randrange(0, 700)
    R = random.randrange(0, 256)
    G = random.randrange(0, 256)
    B = random.randrange(0, 256)
    pygame.draw.lines(screen, (R,G,B), False, [(x1,y1),(x2,y2)], 1)
    pygame.display.update()
