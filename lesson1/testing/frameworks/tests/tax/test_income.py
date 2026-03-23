from tax.income import calculator_tax

def test_calculator_tax():
    assert calculator_tax(1000) == 150.0
    assert calculator_tax(1234) == 185.1
    assert calculator_tax(0) == 0.0
    print("test tax passed")