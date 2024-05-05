class Dog:
    def __init__(self, Имя, Порода, Пол, Возраст):
        self.name = Имя
        self.breed = Порода
        self.gender = Пол
        self.age = Возраст

    def describe(self):
        return f"{self.name} - {self.gender} {self.breed}, {self.age} года"

Chappy = Dog("Chappy", "Пекинес", "Кобель", 3)

print("Информация о собаке:")
print(Chappy.describe())

