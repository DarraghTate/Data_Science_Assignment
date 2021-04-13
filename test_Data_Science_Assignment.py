# Dublin Airport Weather Data Science Assignment by A00288436

from pytest import approx
from Mathematical_Functions import *
from Get_Seasonal_Data import get_extremes

# Mathematical_Functions
def test_get_mean():
    assert get_mean([1,2,3,4,5]) == 3
    assert get_mean([5,4,3,2,1]) == 3
    assert get_mean([1]) == 1
    assert get_mean([-1,-10]) == -5.5

def test_get_mode():
    assert get_mode([1,2,3,4,5,5]) == 5
    assert get_mode([-1, True, True, 4]) == True
    assert get_mode({1: 4, 2: 4, 3: -1, 4: 64}) == 4
    assert get_mode([]) == None

def test_get_median():
    assert get_median([1,2,3,4,5]) == 3
    assert get_median([1,2,3,4,5,6]) == 3.5
    assert get_median([-1, 5, 3]) == 3
    assert get_median({1:-1, 2:5, 3:3}) == (3, 3)

def test_get_standard_deviation():
    assert get_standard_deviation([1,2,3,4,5]) == approx (1.58, 0.01)
    assert get_standard_deviation([5,2,4,1,3]) == approx (1.58, 0.01)
    assert get_standard_deviation([5,2,4,1,False,3]) == approx (1.87, 0.01)
    assert get_standard_deviation([5,2,4,1,True,3]) == approx (1.63, 0.01)

# Get_Seasonal_Data

def test_get_extremes():
    assert get_extremes([1, 2, 3, 4, 6]) == (1, 6)
    assert get_extremes({'a': 4, 'b': -2}) ==  (('b', -2), ('a', 4))

# Note: All remaining functions either read the CSV, or have a None return type