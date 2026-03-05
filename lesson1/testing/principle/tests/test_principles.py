#TODO make it with pip install -e .
# in project root_dir after setup.py defined


# Раннее тестирование позволяет сэкономить время позднее
# Тесты показывают наличие ошибок, а не отсутсвие
# Тесты не должны дублировать логику тестируемого кода
# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны обнаруживать новые ошибки (pescicide paradox)
# Тесты покрывают как успешные, так и ошибочные кейсы

from math_demo import add, add_with_bug, tax_calculator_bugged


def test_addition():
    assert add(2,2) == 4
    assert add(0,0) == 0
    assert add(7,6) == 13
    print("Test addition passed")


def test_addition_with_bug():
    assert add_with_bug(2,2) == 4
    assert add_with_bug(0,0) == 0
    assert add_with_bug(7,6) == 13
    print("Test bugged addition passed")

def test_tax_calculator_bugged():
    assert tax_calculator_bugged(1000) == 200
    assert tax_calculator_bugged(5000) == 1000
    assert tax_calculator_bugged(0) == 0
    assert tax_calculator_bugged(234) == 46.8
    assert tax_calculator_bugged(2.34) == 0.47
    print("Test bugged tax calculator passed")


if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_tax_calculator_bugged()
