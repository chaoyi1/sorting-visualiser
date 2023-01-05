import pygame
import random
import sys
from sort import *

WIDTH = 1920
HEIGHT = 1080
BAR_WIDTH = 2

def main():
    pygame.init()

    sorting_algos ={"selection": selection_sort,
                    "bubble": bubble_sort,
                    "insertion": insertion_sort,
                    "merge": merge_sort,
                    "quick": quick_sort}

    pygame.display.set_caption("visualise")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    screen.fill((255, 255, 255))

    array = random.sample(range(1, HEIGHT+1), WIDTH // BAR_WIDTH)
    algo_name = sys.argv[1]
    if algo_name not in sorting_algos:
        raise ValueError("Invalid method name.")

    running = True
    sorted = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not sorted:
            sorting_algos[algo_name](screen, HEIGHT, BAR_WIDTH, array, 0, len(array)-1)
        pygame.display.flip()
    

if __name__ == "__main__":
    main()