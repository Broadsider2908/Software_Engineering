def add_two(user_input):
    try:
        result = 2 + int(user_input)
        print(f"Результат сложения: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

add_two("5")
add_two("4.23")
add_two("abc")
add_two("8")