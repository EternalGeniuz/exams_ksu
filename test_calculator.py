import pytest

from calculator import Calculator


@pytest.fixture()
def calc():
    return Calculator()


list1 = [3000000000, 100000000]


@pytest.mark.parametrize('a, b, expected_result', [(1, 2, 3),
                                                   (1, 1, 2),
                                                   (4, 5, 9),
                                                   (3, -10, -7),
                                                   (3000000000, 100000000, sum(list1))])
def test_add(calc, a, b, expected_result):
    assert calc.add(a, b) == expected_result


def test_subtract(calc):
    assert calc.subtract(2, 1) == 1


def test_multiply(calc):
    assert calc.multiply(2, 3) == 6


def test_divide(calc):
    assert calc.divide(6, 3) == 2


def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(1, 0)


def test_type_error(calc):
    with pytest.raises(TypeError):
        calc.add(4, "2")
