from time import perf_counter

import sorter
from create_game import create_game


def sort():
    initial_bottles, color_num = create_game()
    start_time = perf_counter()
    steps, total_steps = sorter.steps_solver(sorter.sorter(sorter.combinations(initial_bottles)), color_num)
    print(f"\nThere are {total_steps} steps.\n")
    for x in steps:
        print(f"new step found...\n{x}")
    finish_time = perf_counter()
    print(f"It took {finish_time - start_time} seconds for this program to complete.")


sort()
