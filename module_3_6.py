def calculate_structure_sum(data: list):
    total = 0

    if isinstance(data, (int, float)):  # если элемент число то оно добавляется к сумме
        return data
    elif isinstance(data, str):  # если элемент строка добавляется её длина
        return len(data)
    elif isinstance(data, (list, tuple, set)):  # если элемент список, кортеж или множество - обрабатываются элементы рекурсивно
        for item in data:
            total += calculate_structure_sum(item)
    elif isinstance(data, dict):  # если элемент словарь обрабатываются ключи и значения рекурсивно
        for key, value in data.items():
            total += calculate_structure_sum(key)
            total += calculate_structure_sum(value)

    return total
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_sdfs)
print(result)  # ожидаемый результат 99
