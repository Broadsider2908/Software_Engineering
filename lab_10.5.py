# Создаем класс собственного исключения
class CustomException(Exception):
    def __init__(self, message="Это собственное исключение"):
        self.message = message
        super().__init__(self.message)

# Пример использования исключения в первом фрагменте кода
def function_with_exception(x):
    if x < 0:
        raise CustomException("Число не может быть отрицательным")

try:
    function_with_exception(-1)
except CustomException as e:
    print("Первый фрагмент кода вызвал исключение:", e)

# Пример использования исключения во втором фрагменте кода
def another_function(x, y):
    if x == 0 or y == 0:
        raise CustomException("Один из аргументов равен нулю")

try:
    another_function(0, 5)
except CustomException as e:
    print("Второй фрагмент кода вызвал исключение:", e)