my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# переменная для хранения индекса
index = 0

# цикл while продолжается, пока индекс меньше длины списка
while index < len(my_list):
    # если элемент положительный, выводим его
    if my_list[index] >= 0:
        print(my_list[index])
    # иначе, останавливаем цикл
    else:
        break
    # увеличиваем индекс для перехода к следующему элементу
    index += 1