from recursion.recursion import fibonaci

def test_fibo1():
    actual = fibonaci(1)
    expected = 1
    assert actual == expected

def test_fibo2():
    actual = fibonaci(2)
    expected = 1
    assert actual == expected

def test_fibo3():
    actual = fibonaci(3)
    expected = 2
    assert actual == expected

def test_fibo4():
    actual = fibonaci(4)
    expected = 3
    assert actual == expected