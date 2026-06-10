#Создайте класс "Здание" с атрибутами "адрес" и "количество этажей". Напишите метод, который выводит информацию о здании в формате "Адрес: адрес, Количество этажей: этажи".
class Building:
    def __init__(self, address, floors):
        self.address = address
        self.floors = floors

    def show_info(self):
        print(f"Address: {self.address}, Number of floors: {self.floors}")


building = Building("123 Main St", 5)
building.show_info()
