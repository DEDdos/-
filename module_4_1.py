from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Тестовые примеры
result1 = fake_divide(69, 3)       # Деление 69 на 3
result2 = fake_divide(3, 0)        # Деление 3 на 0 (fake_math)
result3 = true_divide(49, 7)       # Деление 49 на 7
result4 = true_divide(15, 0)       # Деление 15 на 0 (true_math)

# Вывод результатов
print(result1)  # 23.0
print(result2)  # Ошибка
print(result3)  # 7.0
print(result4)  # inf
