import pytest

# Импортируем класс двигателя.
from engine_class import Engine

@pytest.fixture(scope='session')
def engine():
    """Фикстура возвращает экземпляр класса двигателя."""
    # print('Engine factory')  # Добавьте вывод сообщения
    return Engine()


# Эта фикстура не возвращает никаких значений, но изменяет объект,
# созданный другой фикстурой.
@pytest.fixture(autouse=True)
def start_engine(engine):  # Вызываем фикстуру получения объекта двигателя.
    """Фикстура запускает двигатель."""
    # Изменяем значение свойства объекта:
    engine.is_running = True
    # print(f'Before test engine.is_running {engine.is_running}')
    yield  # В этот момент начинает выполняться тест.
    engine.is_running = False  # Заглушим двигатель.
    # Распечатаем строчку после выполнения теста и остановки двигателя.
    # print(f'After test engine.is_running {engine.is_running}') 