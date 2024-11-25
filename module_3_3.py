# 1. функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# вызовы функции с разным количеством аргументов
print("Вызов без аргументов:")
print_params()

print("Вызов с одним именованным аргументом:")
print_params(b=25)

print("Вызов с другим именованным аргументом:")
print_params(c=[1, 2, 3])

print("Вызов с тремя переданными аргументами:")
print_params(10, 'Пример', False)

# 2. распаковка параметров
values_list = [3.14, "Python", False]
values_dict = {'a': 42, 'b': 'Значение', 'c': None}

print("Распаковка списка:")
print_params(*values_list)

print("Распаковка словаря:")
print_params(**values_dict)

# 3. распаковка и отдельные параметры
values_list_2 = [54.32, 'Строка']

print("Распаковка и отдельные параметры:")
print_params(*values_list_2, 42)
