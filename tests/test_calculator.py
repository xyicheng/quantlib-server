from quantlibserver.calculator import Calculator
import pytest

def test_calculator_price():
    cal = Calculator()
    result = cal.price(96.2, 57.20, 0.06, 15.67, 6, 0)
    assert result == 38.7