import sys

sys.path.append(r"C:\Users\hp\Repo\water-color-sorter\src")

from src.objects.bottle import Bottle

empty_b = Bottle(0, [0, 0, 0, 0])
filled_b = Bottle(1, [2, 2, 2, 2])
filled2_b = Bottle(2, [3, 3, 3, 3])
mixed_b = Bottle(3, [2, 3, 4, 1])
mixed2_b = Bottle(4, [5, 5, 6, 4])
mixed3_b = Bottle(5, [0, 5, 5, 5])
mixed4_b = Bottle(6, [0, 0, 5, 3])
mixed5_b = Bottle(7, [0, 5, 6, 6])
mixed6_b = Bottle(8, [0, 2, 2, 2])


def test_top_color():
    assert empty_b.top_color() == (0, 0, 3)
    assert filled_b.top_color() == (2, 0, 3)
    assert mixed_b.top_color() == (2, 0, 0)
    assert mixed6_b.top_color() == (2, 1, 3)


def test_top_color_true():
    assert empty_b.top_color(True) == (0, 4)
    assert mixed2_b.top_color(True) == (5, 2)
    assert mixed3_b.top_color(True) == (5, 2)
    assert mixed6_b.top_color(True) == (2, 3)


def test_can_contain():
    assert empty_b.can_contain(filled_b) is False
    assert empty_b.can_contain(mixed_b) is True
    assert empty_b.can_contain(filled2_b) is False
    assert mixed4_b.can_contain(mixed3_b) is False
    assert empty_b.can_contain(mixed6_b) is False
    assert mixed6_b.can_contain(mixed_b) is True
    assert mixed5_b.can_contain(mixed3_b) is False


def test_is_one_color():
    assert mixed_b.is_one_color() is False
    assert filled_b.is_one_color() is True
    assert filled2_b.is_one_color() is True
    assert mixed6_b.is_one_color() is True


def test_add():
    # empty_b.add(filled_b)
    # assert empty_b.top_color() == (2, 0, 3)
    mixed4_b.add(mixed5_b)
    assert mixed4_b.top_color() == (5, 1, 2)
    empty_b.add(mixed_b)
    assert empty_b.top_color() == (2, 3, 3)


def test_is_sorted():
    assert empty_b.is_sorted() is False
    assert filled_b.is_sorted() is True
    assert filled2_b.is_sorted() is True
    assert mixed6_b.is_sorted() is False
    assert mixed2_b.is_sorted() is False


def test_is_filled():
    assert empty_b.is_filled() is False
    assert filled_b.is_filled() is True
    assert filled2_b.is_filled() is True
    assert mixed6_b.is_filled() is False


def test_is_empty():
    assert mixed_b.is_empty() is False
    assert empty_b.is_empty() is True
    assert filled_b.is_empty() is False
