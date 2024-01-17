import time
from multiprocessing import Process

start = time.perf_counter()


def say_hello():
    time.sleep(1)
    print("helo")


# say_hello()
# say_hello()
# say_hello()
# print(time.perf_counter() - start)
if __name__ == "__main__":
    process_1 = Process(target=say_hello)
    process_2 = Process(target=say_hello)
    process_3 = Process(target=say_hello)
    process_4 = Process(target=say_hello)
    process_5 = Process(target=say_hello)
    process_6 = Process(target=say_hello)
    process_7 = Process(target=say_hello)
    process_8 = Process(target=say_hello)
    process_9 = Process(target=say_hello)
    process_10 = Process(target=say_hello)
    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()
    process_5.start()
    process_6.start()
    process_7.start()
    process_8.start()
    process_9.start()
    process_10.start()
    # print("Joining")
    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()
    process_5.join()
    process_6.join()
    process_7.join()
    process_8.join()
    process_9.join()
    process_10.join()
    print("Time taken:", time.perf_counter() - start)


# nums = [0, 0, 0, 0, 0, 7]
#
# color = 0
# start = 0
# stop = -1
# for x in nums:
#     if x != 0 and color == 0:
#         color = x
#         start = nums.index(x)
#     elif x != color:
#         break
#     stop += 1
# print(color, start, stop)


# def ret():
#     return 2, 3, 34
#
#
# print(ret()[2])

# pl = [1, 3, 4]
# pl.insert(0, 2)
# print(pl)


# hy = [1, 2, 3]
# hy.reverse()
# for x in hy:
#     print(x)


# def ch(b: str):
#     return b[1:]
#
#
# class Hey:
#     def __init__(self, var):
#         self.var = ch(var)
#
#
# p = Hey("joy")
# print(p.var)

# print({(1, 2): [1]})
# print((1,2)+[1])


# dl = [1, 1, 1, 2]
# for x in dl:
#     dl[dl.index(x)] = 0
#
# print(dl)


# def edit(a):
#     a.pop(0)
#
#
# def hi(names):
#     edit(names)
#     for x in names:
#         print(x)


# hi([0, 2, 3, 4])
# print("\n\n")
# bg = [1, 2, 3, 4]
# n = 0
# while n < len(bg):
#     print(bg[n])
#     if bg[n] % 2 == 0:
#         bg.pop(n)
#         continue
#     n += 1
# print(bg)


# vl = [2, 3, 4]
# vl.reverse()
# print(vl)


# from copy import deepcopy
#
#
# class Human:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
#
#     def __str__(self) -> str:
#         return f"My name is {self.name}\nI am {self.age} years old!"
#
#
# person = Human("Collins", 26)
# # print(person)
# humans = []
# for x, y in {"Collins": 21, "Chidera": 22, "Chukwuma": 26}.items():
#     humans.append(Human(x, y))
#
# humans2 = deepcopy(humans)
# for x in humans2:
#     x.age = 19
# for x in humans:
#     print(x.age)
# for c in humans2:
#     print(c)


# def say_hi():
#     return "Hi"


# here = [1, 2, 3, 4, 5]
# print(here[:3])


# from copy import deepcopy
# from src.objects.steps import Steps
# from src.objects.bottle import Bottle
#
# b1 = Bottle(0, [1, 1, 2, 2])
# b2 = Bottle(1, [2, 2, 1, 1])
# b3 = Bottle(2, [0, 0, 0, 0])
# bottles = [b1, b2, b3]
# steps = []
# b3.add(b1)
# copied_bottles = deepcopy(bottles)
# steps.append(Steps(copied_bottles[0].id, copied_bottles[2].id, copied_bottles))
# b1.add(b2)
# copied_bottles = deepcopy(bottles)
# steps.append(Steps(copied_bottles[1].id, copied_bottles[0].id, copied_bottles))
# b3.add(b2)
# copied_bottles = deepcopy(bottles)
# steps.append(Steps(copied_bottles[1].id, copied_bottles[2].id, copied_bottles))
# for i in range(1, 3):
#     steps[i].update(steps[i-1])
# for x in steps:
#     print(f"{steps.index(x)}: {x}\n\n")
#     print(len(x.unsorted_colors))
#     if x.is_sorted() >= 2:
#         for a in x.sorted_colors:
#             print(a)





