import sys

sys.path.append(r"\Users\hp\Repo\water-color-sorter\src")

from src.create_game import create_game


def test_create_game():
    assert create_game()[0][0] == "b0: 1 1 1 1"
