import pytest
import sys
sys.path.append('../src')
import  calculator

def test_calculator_sum():
    add = calculator.findSum("3,2,4")
    assert add == 9

def test_calculator_prod():
    multiply = calculator.findProd("3,3,2")
    assert multiply == 18