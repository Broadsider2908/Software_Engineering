class Dog:
    def __init__(self, Имя, Порода, Пол, Возраст):
        self._name = Имя
        self._breed = Порода
        self._gender = Пол
        self._age = Возраст

    def describe(self):
        return f"{self._name} - {self._gender}, {self._breed}, {self._age} года"

    def speak(self):
        return "Гав-гав!"

class GuideDog(Dog):
    def __init__(self, Имя, Порода, Пол, Возраст, Обучен=True):
        super().__init__(Имя, Порода, Пол, Возраст)
        self._trained = Обучен

    def guide(self):
        if self._trained:
            return f"{self._name} помогает ведомому."
        else:
            return f"{self._name} еще не обучен."

    def speak(self):
        return "Гав-гав! И я помогаю людям!"

Chappy = Dog("Chappy", "Пекинес", "Кобель", 3)

Buddy = GuideDog("Buddy", "Лабрадор", "Кобель", 4)

print("Информация о собаке:")
print(Chappy.describe())

print("\nИнформация о собаке-проводнике:")
print(Buddy.describe())

print("\nСобака говорит:")
print(Chappy.speak())

print("\nСобака-проводник говорит:")
print(Buddy.speak())