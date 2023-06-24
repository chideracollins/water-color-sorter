import sys
from copy import deepcopy

sys.path.append(r"C:\Users\hp\Repo\water-color-sorter\src")

from src.objects.steps import Steps
from src.objects.bottle import Bottle

b1 = Bottle(0, [1, 1, 2, 2])
b2 = Bottle(1, [2, 2, 1, 1])
b3 = Bottle(2, [0, 0, 0, 0])
bottles = [b1, b2, b3]
steps = []
b3.add(b1)
copied_bottles = deepcopy(bottles)
steps.append(Steps(copied_bottles[0].id, copied_bottles[2].id, copied_bottles))
b1.add(b2)
copied_bottles = deepcopy(bottles)
steps.append(Steps(copied_bottles[1].id, copied_bottles[0].id, copied_bottles))
b3.add(b2)
copied_bottles = deepcopy(bottles)
steps.append(Steps(copied_bottles[1].id, copied_bottles[2].id, copied_bottles))
for x in steps:
    print(f"{steps.index(x)}: {x}\n\n")

