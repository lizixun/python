import pygame
import sys


pygame.init()
color = (0, 0, 255)
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("消灭麻子")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event.key.rect = pygame.Rect(0, 0, 3, 3)
            pygame.draw.rect(screen,(230,230,230),event.key.rect)
    screen.fill(color)
    pygame.display.flip()
