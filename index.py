import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

white = (255, 255, 255)
black = (0, 0, 0)
grey = (112, 128, 144)

screen_w = screen.get_width()
screen_h = screen.get_height()

circle_y = screen_h / 2
circle1_x = screen_w * .25
circle2_x = screen_w * .5
circle3_x = screen_w * .75
circle_rad = (circle2_x - circle1_x) / 3

subs_text_x = screen_w * .25
subs_text_y = screen_h * .3

views_text_x = screen_w * .49
views_text_y = screen_h * .3

videos_text_x = screen_w * .75
videos_text_y = screen_h * .3

channel_text_x = screen_w * .10
channel_text_y = screen_h * .1

headerFont = pygame.font.SysFont("Arial", 50)


def draw_hud():
    screen.fill(grey)

    pygame.draw.circle(screen, black, (int(circle1_x), int(circle_y)), int(circle_rad), 5)
    pygame.draw.circle(screen, black, (int(circle2_x), int(circle_y)), int(circle_rad), 5)
    pygame.draw.circle(screen, black, (int(circle3_x), int(circle_y)), int(circle_rad), 5)

    channel_text = headerFont.render("Channel: ", True, black)
    channel_text_loc = channel_text.get_rect(center=(channel_text_x, channel_text_y))
    screen.blit(channel_text, channel_text_loc)

    subs_text = headerFont.render("Subscribers", True, black)
    subs_text_loc = subs_text.get_rect(center=(subs_text_x, subs_text_y))
    screen.blit(subs_text, subs_text_loc)

    views_text = headerFont.render("Views", True, black)
    views_text_loc = views_text.get_rect(center=(views_text_x, views_text_y))
    screen.blit(views_text, views_text_loc)

    videos_text = headerFont.render("Videos", True, black)
    videos_text_loc = videos_text.get_rect(center=(videos_text_x, videos_text_y))
    screen.blit(videos_text, videos_text_loc)


running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.type == QUIT:
                running = False
    draw_hud()
    pygame.display.update()
