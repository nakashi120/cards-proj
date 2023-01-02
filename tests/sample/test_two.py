def test_failing():
    assert(1, 2, 3) == (3, 2, 1)


def test_failing3():
    assert 1 in [2, 3, 4]


def test_failing2():
    assert 'fizz' not in 'fizzbuzz'
