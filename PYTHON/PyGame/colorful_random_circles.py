import pygame
pygame.init()
import random
screen = pygame.display.set_mode((1000,700))
while (True):
    center_x = random.randrange(0, 1000)
    center_y = random.randrange(0, 700)
    radius = random.randrange(10, 50)
    R = random.randrange(0, 256)
    G = random.randrange(0, 256)
    B = random.randrange(0, 256)
    pygame.draw.circle(screen, (R,G,B), [center_x,center_y], radius, 1)
    pygame.display.update()
