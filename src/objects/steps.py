def check_sorted(bottles):
    sorted_ = []
    n = 0
    while n < len(bottles):
        if bottles[n].is_sorted():
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

    def __str__(self):
        return '\n'.join(self.steps)
