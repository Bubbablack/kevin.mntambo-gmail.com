import pytest
import sys
sys.path.append('../src')
import simple

def test_calc_total():
    total = simple.calc_total(3,9)
    assert total == 12

def test_calc_multiply():
    result = simple.calc_multiply(3,3)
    assert result == 9
