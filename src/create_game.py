from objects.bottle import Bottle

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
