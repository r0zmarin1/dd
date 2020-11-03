import pygame
import sys

W = 800
H = 600
collide = False

# квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)
# круг
circle_radius = 35
circle_pos = (0, 0)
# цвет
p = (221, 154, 207)
pp = (231, 102, 208)
pp1 = (238, 0, 209)
BG = (180, 0, 157)

pygame.init()
pygame.display.set_caption('fuyu no hanashi')
screen = pygame.display.set_mode((W, H))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            circle_pos = e.pos
    
    screen.fill(BG)

    rect1 = pygame.draw.circle(screen, pp1, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, p if collide is True else pp, (rect_pos, rect_size))

    if rect1.colliderect(rect2):
        collide = True
    else:
        collide = False

    pygame.display.update()