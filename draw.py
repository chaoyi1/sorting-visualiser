import pygame
import sys

class DrawData:
    def __init__(self, screen_height, screen_width, bar_width, start_x):
        self.start = start_x
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.bar_width = bar_width


def draw_bar(screen, draw_data, x, y, bar_height):
    rect = pygame.Rect(x, y, draw_data.bar_width, bar_height)
    pygame.draw.rect(screen, (0, 0, 0), rect)

def draw_array(screen, draw_data, array):
    screen.fill((255, 255, 255))
    x = draw_data.start
    for height in array:
        y = draw_data.screen_height - height
        draw_bar(screen, draw_data, x, y, height)
        x += draw_data.bar_width
    pygame.display.update()