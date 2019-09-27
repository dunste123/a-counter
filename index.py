import pygame
import youtube
import threading
from StoppableThread import StoppableThread
import sched
import time
import sys
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
circle_rad = (circle2_x - circle1_x) / 2

subs_text_x = screen_w * .25
subs_text_y = screen_h * .25

views_text_x = screen_w * .495
views_text_y = screen_h * .25

videos_text_x = screen_w * .74
videos_text_y = screen_h * .25

channel_text_x = screen_w * .15
channel_text_y = screen_h * .1

channel_name_text_x = screen_w * .5
channel_name_text_y = screen_h * .1

headerFont = pygame.font.SysFont("Arial", 50)
digitFont = pygame.font.SysFont("Arial", 50)

subs = 0
views = 0
videos = 0
channelName = 'null'


def draw_hud():
    screen.fill(grey)

    pygame.draw.circle(screen, black, (int(circle1_x), int(circle_y)), int(circle_rad), 5)
    pygame.draw.circle(screen, black, (int(circle2_x), int(circle_y)), int(circle_rad), 5)
    pygame.draw.circle(screen, black, (int(circle3_x), int(circle_y)), int(circle_rad), 5)

    channel_text = headerFont.render("Channel: ", True, black)
    channel_text_loc = channel_text.get_rect(center=(channel_text_x, channel_text_y))
    screen.blit(channel_text, channel_text_loc)

    subs_text = headerFont.render("Subs", True, black)
    subs_text_loc = subs_text.get_rect(center=(subs_text_x, subs_text_y))
    screen.blit(subs_text, subs_text_loc)

    views_text = headerFont.render("Views", True, black)
    views_text_loc = views_text.get_rect(center=(views_text_x, views_text_y))
    screen.blit(views_text, views_text_loc)

    videos_text = headerFont.render("Videos", True, black)
    videos_text_loc = videos_text.get_rect(center=(videos_text_x, videos_text_y))
    screen.blit(videos_text, videos_text_loc)


running = True
s = sched.scheduler(time.time, time.sleep)


def update_counts(sc):
    global subs, views, videos, channelName
    data = youtube.get_subs_and_views()
    subs = data['subs']
    views = data['views']
    videos = data['videos']
    channelName = data['name']

    # every 60 seconds
    s.enter(60, 1, update_counts, (sc,))


def counter_thread():
    global s
    s.enter(1, 1, update_counts, (s,))
    s.run()


counter_thread = StoppableThread(target=counter_thread, daemon=True)
counter_thread.start()


def run_display():
    global run_thread, running, counter_thread

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.type == QUIT:
                    running = False
                    run_thread.stop()
                    counter_thread.stop()
                    # sys.exit()
        draw_hud()

        subsDisplay = digitFont.render(str(subs), 3, white)
        viewsDisplay = digitFont.render(str(views), 3, white)
        videosDisplay = digitFont.render(str(videos), 3, white)

        subWith, subHeight = digitFont.size(str(subs))
        viewWith, viewHeight = digitFont.size(str(views))
        videoWith, videoHeight = digitFont.size(str(videos))

        screen.blit(subsDisplay, (circle1_x - (subWith / 2), circle_y - 32))
        screen.blit(viewsDisplay, (circle2_x - (viewWith / 2), circle_y - 32))
        screen.blit(videosDisplay, (circle3_x - (videoWith / 2), circle_y - 32))

        channel_name_text = headerFont.render(channelName, True, white)
        channel_name_text_loc = channel_name_text.get_rect(center=(channel_name_text_x, channel_name_text_y))
        screen.blit(channel_name_text, channel_name_text_loc)

        pygame.display.update()
        pygame.display.flip()


run_thread = StoppableThread(target=run_display, daemon=True)
run_thread.run()
