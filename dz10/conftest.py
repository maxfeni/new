import pytest
import time

@pytest.fixture()
def time_test():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f" Время выполнения теста: {end_time-start_time}")


@pytest.fixture(scope="class")
def class_fixture():
    secs = time.time()
    start_time = time.ctime(secs)
    yield
    secs = time.time()
    end_time = time.ctime(secs)
    print(f"Время начала выполнения класса тестов: {start_time}")
    print(f"Время окончания выполнения класса тестов: {end_time}")
