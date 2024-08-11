import pygame
import random
import math
import time

pygame.init()

# The DrawInformation class is used for storing
# and managing information related to drawing elements
# in the window
class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 128, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (2, 47, 255), # picks one of 3 random colours for bar
        (97, 165, 255), # larger number is darkest, smaller number is lightest
        (28, 118, 247), # goes in 3's
    ]

    SMALL_FONT = pygame.font.SysFont("timesnewroman", 15)
    FONT = pygame.font.SysFont("timesnewroman", 25)
    LARGE_FONT = pygame.font.SysFont("timesnewroman", 30)

    SIDE_PAD = 100 # padding for bars
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width     
        self.height = height

        self.window = pygame.display.set_mode((width, height)) # dimensions for window
        pygame.display.set_caption("Algorithm Visualiser")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst)) # width for bars
        self.block_height = math.floor( # round down to nearest integer
            (self.height - self.TOP_PAD) / (self.max_value - self.min_value)
        ) # height for bars
        self.start_x = self.SIDE_PAD // 2 # start position for bars


def draw(draw_info, algo_name, ascending):

    # draw function is responsible for rendering the sorting visualisation on the screen

    # draw_info: is an object that contains information about the drawing
    # window and other drawing-related properties. Includes attributes such as window (the drawing window), BACKGROUND_COLOR, LARGE_FONT (a large font for titles).
    # draw functions are segmented into helper functions
    
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    draw_title(draw_info, algo_name, ascending)
    draw_controls(draw_info)
    draw_sorting_options(draw_info)
    draw_complexity_info(draw_info, algo_name)
    draw_bars(draw_info)
    draw_additional_info(draw_info)
    pygame.display.update()
    

def draw_title(draw_info, algo_name, ascending):
    title_text = f"{algo_name} - {'Ascending' if ascending else 'Descending'}"
    title_surface = draw_info.LARGE_FONT.render(title_text, 1, draw_info.GREEN)
    title_x = (draw_info.width - title_surface.get_width()) / 2
    title_y = 0
    draw_info.window.blit(title_surface, (title_x, title_y))
    
def draw_controls(draw_info):
    controls_text = "Q - Quit | R - Reset | SPACE - Start/Resume/Stop | A - Ascending | D - Descending"
    controls_surface = draw_info.FONT.render(controls_text, 1, draw_info.BLACK)
    controls_x = (draw_info.width - controls_surface.get_width()) / 2
    controls_y = draw_info.LARGE_FONT.get_height()
    draw_info.window.blit(controls_surface, (controls_x, controls_y))
    
def draw_sorting_options(draw_info):
    sorting_text = "I - Insertion Sort | B - Bubble Sort | S - Selection Sort | H - Heap Sort"
    sorting_surface = draw_info.FONT.render(sorting_text, 1, draw_info.BLACK)
    sorting_x = (draw_info.width - sorting_surface.get_width()) / 2
    sorting_y = draw_info.LARGE_FONT.get_height() + draw_info.FONT.get_height()
    draw_info.window.blit(sorting_surface, (sorting_x, sorting_y))

def draw_complexity_info(draw_info, algo_name):
    complexities = { # using dictionary to store values
        "Bubble Sort": ("O(n^2)", "O(1)"),
        "Insertion Sort": ("O(n^2)", "O(1)"),
        "Selection Sort": ("O(n^2)", "O(1)"),
        "Heap Sort": ("O(n log n)", "O(1)"),
    }
    time_complexity, space_complexity = complexities.get(algo_name, ("Not specified", "Not specified")) # returns if value doesn't exit
    complexity_text = f"Time Complexity: {time_complexity} | Space Complexity: {space_complexity}"
    complexity_surface = draw_info.SMALL_FONT.render(complexity_text, 1, draw_info.BLACK)
    complexity_x = (draw_info.width - complexity_surface.get_width()) / 2
    complexity_y = draw_info.LARGE_FONT.get_height() + 2 * draw_info.FONT.get_height() + 10
    draw_info.window.blit(complexity_surface, (complexity_x, complexity_y))

def draw_additional_info(draw_info):
    additional_info_text = "Made by Dominic Murphy"
    additional_info_surface = draw_info.SMALL_FONT.render(additional_info_text, 1, draw_info.BLACK)
    additional_info_x = (draw_info.width - additional_info_surface.get_width()) / 2
    additional_info_y = draw_info.LARGE_FONT.get_height() + 2 * draw_info.FONT.get_height() + draw_info.SMALL_FONT.get_height() + 15
    draw_info.window.blit(additional_info_surface, (additional_info_x, additional_info_y))


def draw_bars(draw_info, colour_positions={}, clear_bg=False):
    """
    draw_bars takes a list of values and draws rectangles on a window based on the
    values in the list.
    

    draw_info: object that contains info to draw list.
    color_positions: dictionary that specifies the positions in the list where you want to change the color of the blocks.
    Keys of the dictionary represent positions in list, and the values represent the colour you want to assign to those positions
    clear_bg: is a boolean value that determines whether the background
    of the drawing window should be cleared before drawing the list.
    If True, a rectangle covering the entire drawing window will be filled with the background colour.
    """
    lst = draw_info.lst # get's list to be drawn

    if clear_bg: # clears background where the bars are drawn
        clear_rect = (
            draw_info.SIDE_PAD // 2,
            draw_info.TOP_PAD,
            draw_info.width - draw_info.SIDE_PAD,
            draw_info.height - draw_info.TOP_PAD,
        )
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst): # provides index + value for each item
        x = draw_info.start_x + i * draw_info.block_width # x position for bar is starting x co-ordinate
        # + index of bar * Width bar
        y = draw_info.height - (val - draw_info.min_value) * draw_info.block_height
        # y position for bar is height of window - scaled value of bar
        # normalises the value within the range and scales it to fit the window height
        
        colour = draw_info.GRADIENTS[i % 3]

        if i in colour_positions:
            colour = colour_positions[i]

        pygame.draw.rect(
            draw_info.window, colour, (x, y, draw_info.block_width, draw_info.height)
        )

    if clear_bg:
        pygame.display.update()
        # update portion of the window that was cleared and redrawn to show new bars


def starting_list(n, min_value, max_value):
    """
    Generates a list of random integers within a given range.
    n: Represents the number of elements you want in the list
    min_value: Minimum value that can be found in list
    max_value: Maximum value that can be found in list
    """
    start_list = []

    for _ in range(n):
        value = random.randint(min_value, max_value)
        start_list.append(value)

    return start_list


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    
    start_time = time.time()
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_bars(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True) # bar at index to be green, bar at index to be red
                yield True # yield returns list of values, continues to end of function
                # allows the sorting process to be paused and resumed by the generator.

    end_time = time.time() - start_time
    print(end_time) 
    return lst


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_bars(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True

    return lst


def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if (lst[j] < lst[min_idx] and ascending) or (
                lst[j] > lst[min_idx] and not ascending
            ):
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        draw_bars(draw_info, {i: draw_info.GREEN, min_idx: draw_info.RED}, True)
        yield True

    return lst


def heapify(draw_info, lst, n, i, ascending):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and (
        (lst[left] > lst[largest] and ascending)
        or (lst[left] < lst[largest] and not ascending)
    ):
        largest = left

    if right < n and (
        (lst[right] > lst[largest] and ascending)
        or (lst[right] < lst[largest] and not ascending)
    ):
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        draw_bars(draw_info, {i: draw_info.GREEN, largest: draw_info.RED}, True)
        yield True

        yield from heapify(draw_info, lst, n, largest, ascending)


def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(draw_info, lst, n, i, ascending)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        draw_bars(draw_info, {i: draw_info.GREEN, 0: draw_info.RED}, True)
        yield True

        yield from heapify(draw_info, lst, i, 0, ascending)

    return lst


def main():
    """
    Main function controls the sorting visualisation program, allowing the user to select different
    sorting algorithms and sort the list in ascending or descending order.
    """
    run = True
    clock = pygame.time.Clock()

    n = 100
    min_val = 0
    max_val = 250

    rand_list = starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1000, 750, rand_list)
    sorting = False
    ascending = True
    sorting_paused = False

    sorting_algorithm = bubble_sort # start with bubble sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60) # change to adjust speed of visualisation

        if sorting and not sorting_paused:
            try:
                next(sorting_algorithm_generator) # next item in list (true)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    rnad_list = starting_list(n, min_val, max_val)
                    draw_info.set_list(rand_list)
                    sorting = False
                elif event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(
                        draw_info, ascending
                    )
                elif event.key == pygame.K_RETURN and not sorting:
                    sorting_paused = False
                elif event.key == pygame.K_a and not sorting:
                    ascending = True
                elif event.key == pygame.K_d and not sorting:
                    ascending = False
                elif event.key == pygame.K_i and not sorting:
                    sorting_algorithm = insertion_sort
                    sorting_algo_name = "Insertion Sort"
                elif event.key == pygame.K_b and not sorting:
                    sorting_algorithm = bubble_sort
                    sorting_algo_name = "Bubble Sort"
                elif event.key == pygame.K_h and not sorting:
                    sorting_algorithm = heap_sort
                    sorting_algo_name = "Heap Sort"
                elif event.key == pygame.K_s and not sorting:
                    sorting_algorithm = selection_sort
                    sorting_algo_name = "Selection Sort"
                elif event.key == pygame.K_q:
                    run = False
                elif event.key == pygame.K_SPACE and sorting and not sorting_paused:
                    sorting_paused = True
                elif event.key == pygame.K_SPACE and sorting and sorting_paused:
                    sorting_paused = False

    pygame.quit()


if __name__ == "__main__":
    main()