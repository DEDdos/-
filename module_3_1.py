# инициализация переменной для подсчета вызовов
calls = 0

# функция count_calls для увеличения счетчика вызовов
def count_calls():
    global calls
    calls += 1

# функция string_info возвращает кортеж с длиной строки, строкой в верхнем и нижнем регистрах
def string_info(string):
    count_calls()  # увеличиваем счетчик вызовов
    return len(string), string.upper(), string.lower()

# функция is_contains проверяет наличие строки в списке, игнорируя регистр
def is_contains(string, list_to_search):
    count_calls()  # увеличиваем счетчик вызовов
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search

# пример вызовов функций
print(string_info('Капибара'))
print(string_info('Армагедон'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print("Общее кол-во вызовов:", calls)
