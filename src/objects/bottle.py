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

    def is_one_color(self) -> bool:
        if self.top_color()[2] == 3:
            return True
        return False

    def can_contain(self, another_bottle) -> bool:
        var: list = another_bottle.top_color(True)
        self_values = self.top_color()[:2]
        if var[0] == self_values[0]:
            if var[1] <= self_values[1]:
                return True
        elif self_values[0] == 0:
            if another_bottle.is_one_color():
                return False
            return True
        return False

    def add(self, another_bottle) -> None:
        """"Adds the color to the bottle and removes it from the transfer bottle"""
        color_code, num_rows = another_bottle.top_color(True)
        self.bottle_colors.reverse()
        position = 1
        for x in self.bottle_colors:
            if x == 0 and position <= num_rows:
                self.bottle_colors[self.bottle_colors.index(x)] = color_code
                position += 1
            elif position > num_rows:
                break
        self.bottle_colors.reverse()
        # Removing the color from the transfer bottle
        for x in another_bottle.bottle_colors:
            if x == 0:
                continue
            elif x == color_code:
                another_bottle.bottle_colors[another_bottle.bottle_colors.index(x)] = 0
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
        return f"{self.id}: {' '.join([str(x) for x in self.bottle_colors])}"
