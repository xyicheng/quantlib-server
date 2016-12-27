from calculator import Calculator
import pytest

def test_calculator_price():
    cal = Calculator()
    result = cal.price(1)
    assert result == 43