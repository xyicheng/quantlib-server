from calculator import calculator
import pytest

def test_calculator_price():
    cal = calculator()
    result = cal.price(1)
    assert result == 43