numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# пустые списки для простых и не простых чисел
primes = []
not_primes = []

for number in numbers:
    if number == 1:
        continue

    # флаг для определения простоты числа
    is_prime = True

    # проверка на делители
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break  # если нашли делитель, число не простое, можно выйти из цикла

    if is_prime: primes.append(number)
    else: not_primes.append(number)

# выводим списки простых и не простых чисел
print("Primes:", primes)
print("Not Primes:", not_primes)
