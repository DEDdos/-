def get_matrix(n, m, value):

    if n <= 0 or m <= 0:
        return []

    matrix = []

    for count_strings in range(n):
        row = []
        for count_slobs in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

n = int(input()) # кол-во строк
m = int(input()) # кол-во столбцов
value = input() # значение

result = get_matrix(n, m, value)

print(result)
