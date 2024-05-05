class Dog:
    def __init__(self, Имя, Порода, Пол, Возраст):
        self._name = Имя
        self._breed = Порода
        self._gender = Пол
        self._age = Возраст

    def describe(self):
        return f"{self._name} - {self._gender}, {self._breed}, {self._age} года"

    def get_name(self):
        return self._name

    def get_breed(self):
        return self._breed

    def get_gender(self):
        return self._gender

    def get_age(self):
        return self._age

class GuideDog(Dog):
    def __init__(self, Имя, Порода, Пол, Возраст, Обучен=True):
        super().__init__(Имя, Порода, Пол, Возраст)
        self._trained = Обучен

    def guide(self):
        if self._trained:
            return f"{self.get_name()} помогает ведомому."
        else:
            return f"{self.get_name()} еще не обучен."

Chappy = Dog("Chappy", "Пекинес", "Кобель", 3)

print("Информация о собаке:")
print(Chappy.describe())

Buddy = GuideDog("Buddy", "Лабрадор", "Кобель", 4)

print("\nИнформация о собаке-проводнике:")
print(Buddy.describe())

print(Buddy.guide())