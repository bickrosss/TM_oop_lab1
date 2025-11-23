#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from pair import Pair
from pair import make_pair


def test_pair_creation():
    pair = Pair(3, 14)
    assert pair.first == 3
    assert pair.second == 14


def test_make_pair_function():
    pair = make_pair(2, 5)
    assert pair.first == 2
    assert pair.second == 5


def test_pair_multiply_positive():
    pair = Pair(2, 5)
    result = pair.multiply(2)
    assert result.first == 5
    assert result.second == 0


def test_pair_multiply_negative():
    pair = Pair(1, 5)
    result = pair.multiply(-2)
    assert result.first == -3
    assert result.second == 0


def test_pair_multiply_zero():
    pair = Pair(5, 5)
    result = pair.multiply(0)
    assert result.first == 0
    assert result.second == 0


def test_pair_multiply_large():
    pair = Pair(10, 25)
    result = pair.multiply(100)
    assert result.first == 1025
    assert result.second == 0


def test_pair_display(capsys):
    pair = Pair(3, 14)
    pair.display()
    captured = capsys.readouterr()
    assert "Число: 3.14" in captured.out


def test_make_pair_invalid_first():
    with pytest.raises(SystemExit):
        make_pair("текст", 5)


def test_make_pair_invalid_second():
    with pytest.raises(SystemExit):
        make_pair(2, -3)


if __name__ == "__main__":
    test_pair_creation()
    test_make_pair_function()
    test_pair_multiply_positive()
    test_pair_multiply_negative()
    test_pair_multiply_zero()
    test_pair_multiply_large()
    test_pair_display(None)
    print("Все тесты пройдены!")
    