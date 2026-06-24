# Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства "кличка" и "порода".

class Animal:
    def __init__(self, species, legs_count, fur_color):
        self.species = species
        self.legs_count = legs_count
        self.fur_color = fur_color


class Dog(Animal):
    def __init__(self, species, legs_count, fur_color, nickname, breed):
        super().__init__(species, legs_count, fur_color)
        self.nickname = nickname
        self.breed = breed

    def show_info(self):
        print(
            f"Вид: {self.species}\n"
            f"Количество лап: {self.legs_count}\n"
            f"Цвет шерсти: {self.fur_color}\n"
            f"Кличка: {self.nickname}\n"
            f"Порода: {self.breed}"
        )


dog1 = Dog("Собака", 4, "рыжий", "Рекс", "Лабрадор")

dog1.show_info()
