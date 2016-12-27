from quantlibserver.calculator import Calculator
import pytest

def test_calculator_price():
    cal = Calculator()
    result = cal.price(96.2, 57.20, 0.0006, 0.1567, 0, maturity_yyyy_mm_dd = (2016,11,29), calculation_yyyy_mm_dd = (2016,11,24))
    assert abs(result - 39.0) < 0.001
