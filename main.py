import pygame
import random

pygame.init()
S_W, S_H = 1280, 720
screen = pygame.display.set_mode((S_W, S_H))
pygame.display.set_caption("DVD Bouncing")
pygame.display.set_icon(pygame.image.load("dvd-icon.png").convert_alpha())
running = True
direction = pygame.Vector2(1, 1)
clock = pygame.Clock()

dvd_img = pygame.image.load("dvd.png").convert_alpha()
dvd_dir = pygame.Vector2(1, 1)
dvd_vel = 100
dvd_rect = dvd_img.get_frect(center=(S_W/2, S_H/2))

colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (128, 0, 128)   # Purple
]
color = pygame.Surface(dvd_img.get_size())
color.fill(random.choice(colors))

while running:
    dt = clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("#121313")
    if dvd_rect.bottom >= S_H:
        dvd_rect.bottom = S_H
        dvd_dir.y*=-1
        color.fill(random.choice(colors))
    if dvd_rect.top <= 0:
        dvd_rect.top = 0
        dvd_dir.y*=-1
        color.fill(random.choice(colors))
    if dvd_rect.right >= S_W:
        dvd_rect.right = S_W
        dvd_dir.x*=-1
        color.fill(random.choice(colors))
    if dvd_rect.left <= 0:
        dvd_rect.left = 0
        dvd_dir.x*=-1
        color.fill(random.choice(colors))
    dvd_rect.center += dvd_dir * dvd_vel * dt
    screen.blit(color, dvd_rect)
    screen.blit(dvd_img, dvd_rect)
    pygame.display.update()
pygame.quit()