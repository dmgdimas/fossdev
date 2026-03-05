def add(a, b):
    return a + b

def add_with_bug(a, b):
    return a * b

def tax_calculator_bugged(income):
    tax_rate = 0.2
    return int(income * tax_rate * 100 + 0.5) / 100  