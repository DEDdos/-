grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# преобразуем множество студентов в отсортированный список
students = sorted(students)

# создаём пустой словарь для хранения средней оценки каждого ученика
student_grades_dict = {}

# заполняем словарь именами и их средними баллами
for i, student in enumerate(students):
    student_grades_dict[student] = sum(grades[i]) / len(grades[i])

# выводим результат
print(student_grades_dict)
print(""Hello, it's me!"")