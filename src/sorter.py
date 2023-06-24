from copy import deepcopy
from objects.steps import Steps


def combinations(bottles: list) -> dict[tuple, tuple]:
    combs = {}
    for i in bottles:
        if i.is_empty():
            continue
        for x in bottles:
            if x.is_filled():
                continue
            i_index = bottles.index(i)
            x_index = bottles.index(x)
            if i_index == x_index:
                continue
            if x.can_contain(i):
                temp_bottles = deepcopy(bottles)
                i_copy = temp_bottles.pop(i_index)
                if i_index < x_index:
                    x_index -= 1
                x_copy = temp_bottles.pop(x_index)
                combs[tuple(temp_bottles)] = (i_copy, x_copy)
    return combs


def sorter(comb: dict):
    steps_ = []
    for x, y in comb.items():
        y[1].add(y[0])
        steps_.append(Steps(y[0].id, y[1].id, list(x + y)))
    return steps_


def find_steps(_step: Steps):
    combs = combinations(_step.unsorted_colors)
    if len(combs) > 0:
        steps_ = sorter(combs)
        for x in steps_:
            copy_step = deepcopy(_step)
            x.update(copy_step)
        return steps_
    return None


def steps_solver(_steps, col_num):
    new_steps = []
    best_final_steps = []
    count_steps = 0
    while True:
        for each_step in _steps:
            steps = find_steps(each_step)
            if steps is None:
                count_steps += 1
                if len(each_step.sorted_colors) == col_num:
                    try:
                        if len(best_final_steps[0].steps) > len(each_step.steps):
                            best_final_steps.clear()
                            best_final_steps.append(each_step)
                        elif len(best_final_steps[0].steps) == len(each_step.steps):
                            best_final_steps.append(each_step)
                    except IndexError:
                        best_final_steps.append(each_step)
                continue
            new_steps.extend(steps)
        if len(new_steps) < 1:
            break
        _steps = deepcopy(new_steps)
        new_steps.clear()
    return best_final_steps, count_steps
