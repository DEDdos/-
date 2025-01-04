def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # вызов inner_function внутри test_function
    inner_function()


# вызов test_function
test_function()

# попытка вызова inner_function вне test_function
try:
    inner_function()
except NameError as e:
    print(f"Ошибка: {e}")
