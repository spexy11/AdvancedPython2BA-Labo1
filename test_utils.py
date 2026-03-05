import pytest
import math
from utils import fact, roots


def test_fact_standard():
    assert fact(5) == 120
    assert fact(3) == 6
    assert fact(1) == 1


def test_fact_zero():
    assert fact(0) == 1


def test_fact_negative():
    with pytest.raises(ValueError, match="must be positive"):
        fact(-1)


# --- Tests pour la fonction roots ---


def test_roots_two_solutions():
    # x^2 - 5x + 6 = 0 -> racines (3, 2)
    res = roots(1, -5, 6)
    assert 3.0 in res
    assert 2.0 in res
    assert len(res) == 2


def test_roots_one_solution():

    res = roots(1, -2, 1)
    assert res == (1.0, 1.0)


def test_roots_no_solution():
    # x^2 + 0x + 1 = 0 -> Delta < 0
    assert roots(1, 0, 1) == ()


def test_roots_float_values():
    # Test avec des nombres à virgule
    a, b, c = 1, 0, -2  # x^2 - 2 = 0 -> racines +/- sqrt(2)
    res = roots(a, b, c)
    assert math.isclose(res[0], math.sqrt(2))
    assert math.isclose(res[1], -math.sqrt(2))
