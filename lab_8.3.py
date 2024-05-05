class Dog:
    def __init__(self, Имя, Порода, Пол, Возраст):
        self.name = Имя
        self.breed = Порода
        self.gender = Пол
        self.age = Возраст

    def describe(self):
        return f"{self.name} - {self.gender}, {self.breed}, {self.age} года"

Chappy = Dog("Chappy", "Пекинес", "Кобель", 3)

print("Информация о собаке:")
print(Chappy.describe())
class GuideDog(Dog):
    def __init__(self, Имя, Порода, Пол, Возраст, Обучен=True):
        super().__init__(Имя, Порода, Пол, Возраст)
        self.trained = Обучен

    def guide(self):
        if self.trained:
            return f"{self.name} помогает ведомому."
        else:
            return f"{self.name} еще не обучен."

Buddy = GuideDog("Buddy", "Лабрадор", "Кобель", 4)

print("\nИнформация о собаке-проводнике:")
print(Buddy.describe())

print(Buddy.guide())