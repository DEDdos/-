class House:
    houses_history = []

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

    def __eq__(self, other):
        """Сравнивает количество этажей между зданиями."""
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        """Определяет поведение оператора <."""
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        """Определяет поведение оператора <=."""
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        """Определяет поведение оператора >."""
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        """Определяет поведение оператора >=."""
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        """Определяет поведение оператора !=."""
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        """Увеличивает количество этажей."""
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        raise TypeError("Можно добавлять только целое число.")

    def __radd__(self, value):
        """Поддерживает обратное сложение."""
        return self.__add__(value)

    def __iadd__(self, value):
        """Поддерживает сложение с присваиванием."""
        return self.__add__(value)

    def __new__(cls, *args, **kwargs):
        """Создание нового дома"""
        house_name = args[0]
        cls.houses_history.append(house_name)
        return super().__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        """Удаление дома"""
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)