import pytest
import Source.my_functions as my_functions
from Source.my_functions import divide


def test_add():
    result1 = my_functions.add(1, 4)
    assert result1 == 5
# Testing second function
def test_devide():
    result2 = my_functions.divide(16, 4)
    assert result2 == 4

def test_sum():
    resutl3 = my_functions.sum(2, 4)
    assert resutl3 == 6;

def test_even():
    result4 = my_functions.is_even(32)


