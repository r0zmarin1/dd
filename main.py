import pygame
import sys

W = 800
H = 600
collide = False
collide2 = False
n = 0
n1 = 0

# квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)
# круг
circle_radius = 35
circle_pos = (0, 0)
# цвет
p = (221, 154, 207, 180)
pp = (231, 102, 208, 180)
pp1 = (238, 0, 209, 180)
BG = (180, 0, 157)

pygame.init()
pygame.display.set_caption('yarichin B-club')
screen = pygame.display.set_mode((W, H))
font = pygame.font.Font(None, 32)
font2 = pygame.font.Font(None, 32)
# создаем поверхность размером в 2 раза больше радиуса круга и вкл. альфа-канал
surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
# на созданной поверхности рисуем круг pp1 цвета
pygame.draw.circle(surface, pp1, (circle_radius, circle_radius), circle_radius)
# находим рект у поверхности
rect1 = surface.get_rect()

clock = pygame.time.Clock()
FPS = 660
speed = [1, 1]

ball = pygame.image.load('ball.png')
ball_rect = ball.get_rect()


def abc(x, y):
    if ball_rect.left < 0 or ball_rect.right > W:
        speed[0] = -x
    if ball_rect.top < 0 or ball_rect.bottom > H:
        speed[1] = -y
    return ball_rect.move(speed)


while True:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            # circle_pos = e.pos
            rect1.center = e.pos

    ball_rect = abc(speed[0], speed[1])

    screen.fill(BG)
    COLOR = p if collide or collide2 else pp
    # rect1 = pygame.draw.circle(screen, pp1, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, COLOR, (rect_pos, rect_size))
    screen.blit(surface, rect1)

    if rect1.colliderect(rect2):
        if not collide:
            collide = True
            n += 1
    else:
        collide = False

    if ball_rect.colliderect(rect2):
        if not collide2:
            collide2 = True
            n1 += 1
    else:
        collide2 = False

    screen.blit(ball, ball_rect)
    screen.blit(font.render(str(n), 1, p), (10, 10))
    screen.blit(font2.render(str(n1), 1, p), (770, 10))
    pygame.display.update()
