import pytest
from tax import calculate_tax

def test_calculate_tax():
    assert calculate_tax(1000) == 150.0
    assert calculate_tax(1234) == 185.1
    assert calculate_tax(0) == 0.0
    print("test tax passed")

def test_calculate_tax_integer_cents():
    assert calculate_tax(1000.99) == 150.15
    assert calculate_tax(1234.56) == 185.18
    print("test tax with integer cents passed")

@pytest.mark.parametrize("income, expected_tax", [
    (1000, 150.0),
    (1234, 185.1),
    (0, 0.0)
])
def test_calculate_tax_parametrized(income, expected_tax):
    assert calculate_tax(income) == expected_tax
    print(f"test tax passed for income {income}")