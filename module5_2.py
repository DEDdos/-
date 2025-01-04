class House:
    def __init__(self, name, number_of_floors):
        """Инициализация объекта класса House."""
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """Метод для перемещения на заданный этаж."""
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        """Возвращает количество этажей в здании."""
        return self.number_of_floors

    def __str__(self):
        """Возвращает строку с описанием здания."""
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20

print(len(h1))  # 10
print(len(h2))  # 20
