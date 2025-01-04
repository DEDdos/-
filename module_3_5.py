def get_multiplied_digits(number):
    # преобразуем число в строку
    str_number = str(number)

    # получаем первую цифру числа
    first = int(str_number[0])

    # базовый случай: если длина строки равна 1, возвращаем первую цифру
    if len(str_number) == 1:
        return first

    # рекурсивный случай: умножаем первую цифру на результат работы функции с остальной частью числа
    return first * get_multiplied_digits(int(str_number[1:]))

# тестируем функцию
result = get_multiplied_digits(40203)
print(result)  # ожидаемый результат: 24

result2 = get_multiplied_digits(402030)
print(result2)  # ожидаемый результат: 24
