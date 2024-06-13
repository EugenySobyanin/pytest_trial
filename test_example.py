# test_example.py
import pytest


def one_more(x):
    return x + 1


def get_sort_list(str):
    new_list = sorted(str.split(', '))
    return new_list


@pytest.mark.parametrize(
    'input_arg, expected_result',
    [
        (4, 5),
        pytest.param(3, 5, marks=pytest.mark.xfail)  # ожидается падение теста с этими параметрами
    ]
)
def test_one_more(input_arg, expected_result):
    assert one_more(input_arg) == expected_result
    


def test_sort():
    """Тестируем функцию get_sort_list()."""    
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result == ['Даша', 'Маша', 'Саша', 'Яша']


def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    # Провальный тест:
    # ожидаем число, но вернётся список.
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert isinstance(result, int)
    
    
@pytest.mark.skip(reason='Это был пример как ожидаемо падающий тест проходит.')
@pytest.mark.xfail(reason='Пусть пока падает, завтра починю.')
def test_false():
    assert False
    
    
    
def cartesian_product(a, b):
    return a * b


@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', ['one', 'two'])
def test_cartesian_product(x, y):
    assert cartesian_product(x, y) is not None 
