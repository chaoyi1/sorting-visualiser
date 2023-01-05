import pygame
from draw import *

def selection_sort(screen, screen_height, bar_width, array, l, r):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        draw_array(screen, screen_height, bar_width, 0, array)
        pygame.time.wait(10)

def bubble_sort(screen, screen_height, bar_width, array, l, r):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        draw_array(screen, screen_height, bar_width, 0, array)
        pygame.time.wait(10)

def insertion_sort(screen, screen_height, bar_width, array, l, r):
    n  = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        draw_array(screen, screen_height, bar_width, 0, array)
        pygame.time.wait(10)

def merge(screen, screen_height, bar_width, array, l, mid, r):
    n1 = mid - l + 1
    n2 = r - (mid + 1) + 1
    L = [0 for _ in range(n1)]
    R = [0 for _ in range(n2)]
    for i in range(n1):
        L[i] = array[l+i]
    for j in range(n2):
        R[j] = array[mid+1+j]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1
    draw_array(screen, screen_height, bar_width, 0, array)
    pygame.time.wait(10)

def merge_sort(screen, screen_height, bar_width, array, l, r):
    if (l < r):
        mid = l + (r - l) // 2
        merge_sort(screen, screen_height, bar_width, array, l, mid)
        merge_sort(screen, screen_height, bar_width, array, mid+1, r)
        merge(screen, screen_height, bar_width, array, l, mid, r)

def partition(screen, screen_height, bar_width, array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    draw_array(screen, screen_height, bar_width, 0, array)
    pygame.time.wait(10)
    return i + 1

def quick_sort(screen, screen_height, bar_width, array, l, r):
    if l < r:
        pivot_index = partition(screen, screen_height, bar_width, array, l, r)
        quick_sort(screen, screen_height, bar_width, array, l, pivot_index - 1)
        quick_sort(screen, screen_height, bar_width, array, pivot_index+1, r)