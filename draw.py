import pygame
import sys

def draw_bar(screen, bar_width, bar_height, x, y):
    rect = pygame.Rect(x, y, bar_width, bar_height)
    pygame.draw.rect(screen, (0, 0, 0), rect)

def draw_array(screen, screen_height, bar_width, x, array):
    screen.fill((255, 255, 255))
    for height in array:
        y = screen_height - height
        draw_bar(screen, bar_width, height, x, y)
        x += bar_width
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()