from script import sum, devide

def test_sum():
    a = 1
    b = 2
    result = 3
    assert sum(a,b) == result

def test_devide():
    a = 2
    b = 4
    result = 0.5
    assert devide(a,b) == result

def test_division_prohibited():
    try:
        devide("A","B")
        print("Test string-devision fails")
        assert False
    except:
        print("Test string-devision pass")

if __name__=="__main__":
    test_devide()
    test_sum()
    test_division_prohibited()
