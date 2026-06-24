#Создайте класс "Здание" с атрибутами "адрес" и "количество этажей". Напишите метод, который выводит информацию о здании в формате "Адрес: адрес, Количество этажей: этажи".

class Building:
    def __init__(self, address, floors):
        self.address = address
        self.floors = floors

    def show_info(self):
        print(f"Адрес: {self.address}, Количество этажей: {self.floors}")


building1 = Building("ул. Ленина, 15", 9)

building1.show_info()
