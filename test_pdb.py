import pdb


def integers_counter(data):
    # Создаем счётчик для целых чисел.
    integers_found = 0
    # Перебираем в цикле элементы входного списка.
    for item in data:
        # Если элемент - целое число, то увеличиваем счётчик.
        if isinstance(item, int) and not isinstance(item, bool):
            integers_found += 1
    # Возвращаем счётчик.
    return integers_found


def transform_list(x):
    x.append(1)
    x.extend([2, 3])
    return x


def test_counter():
    # Произвольные данные для анализа.
    data = [False, 1.0, "some_string", 3, True, 1, [], False]
    # pdb.set_trace() # Точка останова. Именно отсюда начнём дебаг
    # Вызываем функцию:
    integers = integers_counter(data)
    # Целых чисел должно быть 2.
    assert integers == 2
    

def test_list():
    a = []
    a = transform_list(a)
    a = [4] + a
    assert a == [1, 2, 3, 4]