import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from shared.py.utils.numbers import normalize_numbers


def test_normalize_simple_number():
    text = "He owes me 5 dollars."
    assert normalize_numbers(text) == "He owes me five dollars."


def test_normalize_money_and_ordinal():
    text = "She won $1.05 in the 1st contest."
    expected = "She won one dollar, five cents in the first contest."
    assert normalize_numbers(text) == expected


def test_decimal_number():
    text = "Pi is 3.14"
    assert normalize_numbers(text) == "Pi is three point fourteen"
