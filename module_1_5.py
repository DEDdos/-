immutable_var = (2, 6.3, "переменная", True)
print("Неизменяемый кортеж: ", immutable_var)

# попытка изменить неизменяемый кортеж
# immutable_var[0] = 5

# изменение данных в неизменяемом котреже приведёт к ошибке

# пояснение:
# кортежи — это неизменяемые объекты, и мы не можем изменять их элементы после создания.
# если попытаться сделать это, Python выдаст ошибку - TypeError: 'tuple' object does not support item assignment.

mutable_var = [2, 6.3, "переменная", True]
print("изменяемый кортеж ДО изменений: ", mutable_var)

mutable_var[0] = 5
mutable_var[1] = 8.9
mutable_var[2] = "НЕпеременная"
mutable_var[3] = False

print("изменяемый кортеж ПОСЛЕ изменений: ",mutable_var)