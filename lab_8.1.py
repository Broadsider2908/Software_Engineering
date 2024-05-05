class Dog:
    def __init__(self, Имя, Порода, Пол):
        self.name = Имя
        self.breed = Порода
        self.gender = Пол

Chappy = Dog("Chappy", "Пекинес", "Кобель")

print(f"Имя собаки: {Chappy.name}")
print(f"Порода: {Chappy.breed}")
print(f"Пол: {Chappy.gender}")