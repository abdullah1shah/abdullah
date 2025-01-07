import pytest

# Fixture with parameterized tuples
@pytest.fixture
def number_tuples():
    return [
        (2, 3),  # Test tuple 1
        (4, 5),  # Test tuple 2
        (7, 2),  # Test tuple 3
        (10, 0)  # Test tuple 4 (to check division by zero)
    ]

# Test addition
@pytest.mark.parametrize("a, b", [(2, 3), (4, 5), (7, 2)])
def test_addition(a, b):
    assert a + b == a + b

# Test multiplication
@pytest.mark.parametrize("a, b", [(2, 3), (4, 5), (7, 2)])
def test_multiplication(a, b):
    assert a * b == a * b

# Test division
@pytest.mark.parametrize("a, b", [(2, 3), (4, 2), (7, 2), (10, 0)])
def test_division(a, b):
    if b == 0:
        with pytest.raises(ZeroDivisionError):
            a / b
    else:
        assert a / b == a / b
