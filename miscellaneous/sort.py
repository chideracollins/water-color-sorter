from copy import deepcopy

COLOR_CODES = {
    0: 'Empty',
    1: 'Red',
    2: 'Green',
    3: 'Blue',
    4: 'Yellow',
    5: 'Orange',
    6: 'Pink',
    7: 'Gray',
    8: 'Pale Red',
    9: 'Pale Blue',
    10: 'Deep Blue',
    11: 'Light Green',
    12: 'Light Yellow',
}
STEPS = []


class Bottle:
    def __init__(self, index: int, bottle_colors: list) -> None:
        self.id = f"b{index}"
        self.bottle_colors = bottle_colors

    def top_color(self, color_len: bool = False):
        color = 0
        start = 0
        stop = -1
        for x in self.bottle_colors:
            if x != 0 and color == 0:
                color = x
                start = self.bottle_colors.index(x)
            elif x != color:
                break
            stop += 1
        if color_len:
            return color, stop - start + 1
        return color, start, stop

    def can_contain(self, var) -> bool:
        self_values = self.top_color()[:2]
        if var[0] == self_values[0]:
            if var[1] <= self_values[1]:
                return True
        elif self_values[0] == 0:
            return True
        return False

    def is_one_color(self) -> bool:
        if self.top_color()[2] == 3:
            return True
        return False

    def add(self, color_code, num_rows) -> None:
        # print(self.bottle_colors)
        self.bottle_colors.reverse()
        position = 1
        for x in self.bottle_colors:
            if x == 0 and position <= num_rows:
                self.bottle_colors[self.bottle_colors.index(x)] = color_code
                position += 1
            elif position > num_rows:
                break
        self.bottle_colors.reverse()
        # print(self.bottle_colors)

    def remove(self, color_code) -> None:
        for x in self.bottle_colors:
            if x == 0:
                continue
            elif x == color_code:
                self.bottle_colors[self.bottle_colors.index(x)] = 0
                continue
            break

    def is_sorted(self) -> bool:
        if self.bottle_colors[0] == 0:
            return False
        first_color = self.bottle_colors[0]
        for x in self.bottle_colors:
            if x != first_color:
                return False
        return True

    def is_filled(self) -> bool:
        if self.bottle_colors[0] != 0:
            return True
        return False

    def is_empty(self) -> bool:
        for color in self.bottle_colors:
            if color != 0:
                return False
        return True

    def __str__(self) -> str:
        return ' '.join([str(x) for x in self.bottle_colors])


def check_sorted(bottles):
    sorted_ = []
    n = 0
    while n < len(bottles):
        if (bottles[n]).is_sorted():
            sorted_.append(bottles.pop(n))
            continue
        n += 1
    return sorted_


class Steps:
    def __init__(self, from_: int, into: int, bottles: list):
        self.steps = [f"{from_} to {into}"]
        self.sorted_colors = check_sorted(bottles)
        self.unsorted_colors = bottles

    def update(self, parent):
        parent.steps.reverse()
        for x in parent.steps:
            self.steps.insert(0, x)
        parent.steps.reverse()
        if len(parent.sorted_colors) > 0:
            for x in parent.sorted_colors:
                self.sorted_colors.append(x)

    def is_sorted(self):
        return len(self.sorted_colors)

    def __str__(self):
        return '\n'.join(self.steps)


def bottle_color(i):
    return [int(x) for x in input(f"Bottle {i}: ").split()]


def create_game() -> tuple[list[Bottle], int]:
    color_coding = input(
        f"{COLOR_CODES}\nPick the colors involved by keying in their color codes, separated by whitespaces: ").split()
    bottle_num = int(input("How many bottles are there? "))
    print("Please provide the color codes for each bottle starting from the first row down to the last row"
          "\nN/B: Start inputting the bottle values from the top left to the bottom right"
          "\nHere are the colors you chose and their color codes, "
          "please ensure to not enter a color code outside these ones")
    for x in color_coding:
        print(f"{x} reps {COLOR_CODES[int(x)]}")
    bottles = []
    for x in range(bottle_num):
        bottles.append(Bottle(x, bottle_color(x)))
    return bottles, len(color_coding) - 1


def rules(b1: Bottle, b2: Bottle) -> bool:
    if b1.is_empty():
        return False
    if b2.is_filled():
        return False
    if b1.is_one_color() and b2.is_empty():
        return False
    return b2.can_contain(b1.top_color(color_len=True))


def combinations(bottles: list):
    combs = {}
    for i in bottles:
        for x in bottles:
            i_index = bottles.index(i)
            x_index = bottles.index(x)
            if i_index == x_index:
                continue
            if rules(i, x):
                print(i, x)
                temp_bottles = deepcopy(bottles)
                temp_bottles.pop(i_index)
                temp_bottles.pop(x_index - 1)
                combs[tuple(temp_bottles)] = tuple([i, x])
    return combs


def sorter(comb: dict):
    steps_ = []
    for x, y in comb.items():
        col, len_ = y[0].top_color(color_len=True)
        y[1].add(col, len_)
        y[0].remove(col)
        print(x)
        steps_.append(Steps(y[0].id, y[1].id, list(x + y)))
    return steps_


def find_steps(_step: Steps):
    combs = combinations(_step.unsorted_colors)
    if len(combs) > 0:
        steps_ = sorter(combs)
        for x in steps_:
            x.update(_step)
        return steps_
    STEPS.append(_step)
    return None


def steps_solver(_steps):
    new_steps = []
    while True:
        for x in _steps:
            steps = find_steps(x)
            if steps is None:
                continue
            new_steps.extend(steps)
        if len(new_steps) < 1:
            break
        _steps = deepcopy(new_steps)
        new_steps.clear()


def sort():
    initial_bottles, to_be_solved = create_game()
    steps_solver(sorter(combinations(initial_bottles)))
    for x in STEPS:
        print(x)
        print("\n\n")
    # if x.is_sorted == to_be_solved:
    #     print("\n\n", x)


# sort()
# import test
import subprocess


subprocess.run("python test.py", shell=True)
