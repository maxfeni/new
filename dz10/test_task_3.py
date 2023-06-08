# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('a, b, result', [
    pytest.param(1, 2, 2.5, marks=pytest.mark.smoke),
    pytest.param(10, -1, -10),
    pytest.param(0, 3, 0),
    pytest.param(1, 1, 1),
    pytest.param(2, 0, ZeroDivisionError, marks=pytest.mark.skip("bad test"))])
def test_division(a, b, result):
    assert all_division(a, b) == result
