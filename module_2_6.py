from random import randrange

def find_password(n):
    result = ""

    # внешний цикл - первое число пары (от 1 до n-1)
    for i in range(1, n):
        # внутренний цикл - второе число пары (от i+1 до n)
        for j in range(i + 1, n):
            # проверяем, делится ли сумма чисел i и j на n
            if (i + j) % n == 0:
                # если условие выполняется, добавляем пару в строку результата
                result += str(i) + str(j)

    return result


### РЕЗУЛЬТАТ ###

## Проверка ввёденных чисел
n = int(input("Введите число от 3 до 20: "))

# проверка исходного числа
if n >= 3 and n <= 20 :
    password = find_password(n)
    print(f"Нужный пароль для введённого числа {n}: {password}")
else: print("Вы ввели неверное число")

## Проверка случайных чисел от 3 до 20
m = int(randrange(3,20))
password = find_password(m)
print(f"Нужный пароль для случайного числа {m}: {password}")