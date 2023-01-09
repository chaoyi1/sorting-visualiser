import pygame
import random
import sys
from sort import *

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BAR_WIDTH = 2

def main():
    pygame.init()

    clock = pygame.time.Clock()

    sorting_algos ={"selection": selection_sort,
                    "bubble": bubble_sort,
                    "insertion": insertion_sort,
                    "merge": merge_sort,
                    "quick": quick_sort}

    pygame.display.set_caption("visualise")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    screen.fill((255, 255, 255))

    draw_data = DrawData(SCREEN_HEIGHT,SCREEN_WIDTH,BAR_WIDTH,0)

    array = random.sample(range(1, SCREEN_HEIGHT+1), SCREEN_WIDTH // BAR_WIDTH)
    algo_name = sys.argv[1]
    if algo_name not in sorting_algos:
        raise ValueError("Invalid method name.")

    running = True
    sorted = False
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if not sorted:
            sorting_algos[algo_name](screen, draw_data, array)
            sorted = True
    

if __name__ == "__main__":
    main()