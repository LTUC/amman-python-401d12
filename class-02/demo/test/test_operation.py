from operation.operation import add, sub, multi, devide

def test_add():
    actual = add(2,3)
    expected = 5
    assert actual == expected

def test_sub():
    actual = sub(10,5)
    expected = 5
    assert actual == expected

def test_multi():
    actual = multi(6,3)
    expected = 18
    assert actual == expected

def test_devide():
    actual = devide(6,3)
    expected = 2
    assert actual == expected