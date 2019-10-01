import pygame
import youtube
import webbrowser
from StoppableThread import StoppableThread
import sched
import time
from pygame.locals import *
from colors import *
from button import Button

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

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

headerFont = pygame.font.SysFont('Arial', 50)
digitFont = pygame.font.SysFont('Arial', 50)
subs = 0
views = 0
videos = 0
channelName = 'null'
latest_video_id = youtube.default_video_id
button_text = 'View latest video'
button_width = len(button_text) * 25
button = Button(green, (screen_w - button_width) / 2, screen_h * .75, button_width, 100, button_text)


def draw_hud():
    screen.fill(grey)
    pygame.draw.circle(screen, black, (int(circle1_x), int(circle_y)), int(circle_rad), 5)
    pygame.draw.circle(screen, black, (int(circle2_x), int(circle_y)), int(circle_rad), 5)
    pygame.draw.circle(screen, black, (int(circle3_x), int(circle_y)), int(circle_rad), 5)

    channel_text = headerFont.render('Channel: ', True, black)
    channel_text_loc = channel_text.get_rect(center=(channel_text_x, channel_text_y))
    screen.blit(channel_text, channel_text_loc)

    subs_text = headerFont.render('Subs', True, black)
    subs_text_loc = subs_text.get_rect(center=(subs_text_x, subs_text_y))
    screen.blit(subs_text, subs_text_loc)

    views_text = headerFont.render('Views', True, black)
    views_text_loc = views_text.get_rect(center=(views_text_x, views_text_y))
    screen.blit(views_text, views_text_loc)

    videos_text = headerFont.render('Videos', True, black)
    videos_text_loc = videos_text.get_rect(center=(videos_text_x, videos_text_y))
    screen.blit(videos_text, videos_text_loc)

    button.draw(screen, black)


running = True
s = sched.scheduler(time.time, time.sleep)


def update_counts(sc):
    global subs, views, videos, channelName, latest_video_id
    data = youtube.get_subs_and_views()
    subs = data['subs']
    views = data['views']
    videos = data['videos']
    channelName = data['name']
    latest_video_id = youtube.get_latest_video_id()
    # every 60 seconds
    s.enter(60, 1, update_counts, (sc,))


def counter_thread():
    global s
    s.enter(1, 1, update_counts, (s,))
    s.run()


def open_video_in_browser():
    webbrowser.open('https://www.youtube.com/watch?v=' + latest_video_id)
    call_quit_event()


def call_quit_event():
    event = pygame.event.Event(QUIT)
    pygame.event.post(event)


counter_thread = StoppableThread(target=counter_thread, daemon=True)
counter_thread.start()


def run_display():
    global run_thread, running, counter_thread

    while running:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONDOWN:
                if button.isOver(pos):
                    open_video_in_browser()
            elif event.type == MOUSEMOTION:
                if button.isOver(pos):
                    button.color = dark_green
                else:
                    button.color = green
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    call_quit_event()
            elif event.type == QUIT:
                running = False
                run_thread.stop()
                counter_thread.stop()
                quit(0)

        draw_hud()

        subs_display = digitFont.render(str(subs), 3, white)
        views_display = digitFont.render(str(views), 3, white)
        videos_display = digitFont.render(str(videos), 3, white)
        sub_with, sub_height = digitFont.size(str(subs))
        view_with, view_height = digitFont.size(str(views))
        video_with, video_height = digitFont.size(str(videos))
        screen.blit(subs_display, (circle1_x - (sub_with / 2), circle_y - 32))
        screen.blit(views_display, (circle2_x - (view_with / 2), circle_y - 32))
        screen.blit(videos_display, (circle3_x - (video_with / 2), circle_y - 32))
        channel_name_text = headerFont.render(channelName, True, white)
        channel_name_text_loc = channel_name_text.get_rect(center=(channel_name_text_x, channel_name_text_y))
        screen.blit(channel_name_text, channel_name_text_loc)
        pygame.display.update()
        pygame.display.flip()


run_thread = StoppableThread(target=run_display, daemon=True)
run_thread.run()
