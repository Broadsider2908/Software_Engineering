import time

class TimerDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {self.func.__name__}: {execution_time} секунд")
        return result

@TimerDecorator
def example_function_1(n):
    # Просто заснем на n секунд
    time.sleep(n)

@TimerDecorator
def example_function_2(a, b):
    # Просто сложим два числа
    return a + b

example_function_1(3)
result = example_function_2(2, 3)
print("Результат выполнения функции example_function_2:", result)