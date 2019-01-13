#!/usr/bin/env python
# -*- coding: utf-8 -*-

from recap.calculation import calculation


""" Average tests 
"""


def test_average_int_result():
    numbers = (1, 5, 6)
    expected = 4
    result = calculation.average(numbers=numbers)
    assert result == expected


def test_average_float_result_rounded_down():
    numbers = (1, 3, 6)
    expected = 3
    result = calculation.average(numbers=numbers)
    assert result == expected


def test_average_float_result_rounded_up():
    numbers = (6, 4, 1)
    expected = 4
    result = calculation.average(numbers=numbers)
    assert result == expected


def test_average_more_input():
    numbers = (6, 4, 1, 10, 11, 18, 20, 52, 85)
    expected = 23
    result = calculation.average(numbers=numbers)
    assert result == expected


""" Min tests 
"""


def test_min_asc():
    numbers = (8, 17, 23, 79, 101, 1005, 999972)
    expected = 8
    result = calculation.min(numbers=numbers)
    assert result == expected


def test_min_desc():
    numbers = (784521, 11005, 452, 18, 0)
    expected = 0
    result = calculation.min(numbers=numbers)
    assert result == expected


def test_min_equal_numbers():
    numbers = (45, 45, 45)
    expected = 45
    result = calculation.min(numbers=numbers)
    assert result == expected


""" Max tests 
"""


def test_max_asc():
    numbers = (8, 17, 23, 79, 101, 1005, 999972)
    expected = 999972
    result = calculation.max(numbers=numbers)
    assert result == expected


def test_max_desc():
    numbers = (784521, 11005, 452, 18, 0)
    expected = 784521
    result = calculation.max(numbers=numbers)
    assert result == expected


def test_max_equal_numbers():
    numbers = (45, 45, 45)
    expected = 45
    result = calculation.max(numbers=numbers)
    assert result == expected


""" Biggest increase
"""


def test_biggest_increase():
    numbers = (480, 500, 980)
    expected = 480
    result = calculation.biggest_increase(numbers=numbers)
    assert result == expected


def test_biggest_increase_with_decrease_in_numbers():
    numbers = (320, 321, 200, 1200, 400)
    expected = 1000
    result = calculation.biggest_increase(numbers=numbers)
    assert result == expected


def test_biggest_increase_with_decreases_only():
    numbers = (5412, 4512, 3000, 1200, 12, 0)
    expected = 0
    result = calculation.biggest_increase(numbers=numbers)
    assert result == expected


def test_biggest_increase_with_equal_numbers():
    numbers = (450, 450, 450, 450, 450)
    expected = 0
    result = calculation.biggest_increase(numbers=numbers)
    assert result == expected


""" Biggest decrease
"""


def test_biggest_decrease():
    numbers = (980, 500, 480)
    expected = 480
    result = calculation.biggest_decrease(numbers=numbers)
    assert result == expected


def test_biggest_decrease_with_increase_in_numbers():
    numbers = (480, 321, 310, 400, 380)
    expected = 159
    result = calculation.biggest_decrease(numbers=numbers)
    assert result == expected


def test_ biggest_decrease_with_increases_only():
    numbers = (12, 485, 2000, 4785, 5007)
    expected = 0
    result = calculation.biggest_decrease(numbers=numbers)
    assert result == expected


def test_biggest_decrease_with_equal_numbers():
    numbers = (450, 450, 450, 450, 450)
    expected = 0
    result = calculation.biggest_decrease(numbers=numbers)
    assert result == expected


""" Total change
"""


def test_total_changes_increase():
    numbers = (450, 800, 450, 500)
    expected = 50
    result = calculation.total_change(numbers=numbers)
    assert result == expected


def test_total_changes_decrease():
    numbers = (500, 300, 200, 2000, 420)
    expected = 80
    result = calculation.total_change(numbers=numbers)
    assert result == expected


def test_total_changes_no_changes():
    numbers = (500, 300, 200, 2000, 500)
    expected = 0
    result = calculation.total_change(numbers=numbers)
    assert result == expected
