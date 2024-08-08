"""Домашнее задание по теме 'Обзор сторонних библиотек Python'"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Использование numpy

a = np.array([1, 2, 3, 4, 5])
b = np.random.random((2, 3))
min_a = np.min(a)            # Минимальное значение массива a
max_a = np.max(a)            # Максимальное значение массива a
sum_a = np.sum(a)            # Сумма элементов массива a

print(f'Созданный массив: {a}')
print(f'Сгенерированная из случайных чисел матрица:\n {b}')
print(f'Минимальное значение массива a: {min_a}')
print(f'Максимальное значение массива a: {min_a}')
print(f'Сумма элементов массива a: {sum_a}')

# Использование pandas
# класс Series
s = pd.Series(a, index=["a", "b", "c", "d", "e"])
print(f'Одномерный массив:\n{s}')
print(f'Выбор одного элемента "a" {s["a"]}')
print(f'Срез [1:]\n{s[1:]}')
print(f'Фильтрация [s > 2]\n{s[s > 2]}')

# класс DataFrame
students_marks_dict = {"student": ["Студент_1", "Студент_2", "Студент_3"],
                       "math": [5, 3, 4],
                       "physics": [4, 5, 5]}

students = pd.DataFrame(students_marks_dict)
print(f'Двухмерный массив:\n{students}')
# запись двухмерного массива в Exsel файл
file = r"proba_1.xlsx"
if os.path.isfile(file):  # если файл уже существует
    with pd.ExcelWriter(file, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        students.to_excel(writer, sheet_name="Студенты", index=False, engine="openpyxl")
else:
    students.to_excel(file, sheet_name="Студенты", index=False, engine="openpyxl")
    students.save(file)
print(f'Двухмерный массив (первые две строки):\n{students.head(2)}')
print(f'Двухмерный массив (последние две строки):\n{students.tail(2)}')
# среднее арифметическое сдачи зачетов (добавлена колонка)
students["total score"] = (students["math"] + students["physics"]) / 2
print(students.sort_values(["total score"], ascending=False).head())

# Использование matplotlib
# Столбчатая диаграмма

x = students["student"]
y_1 = students["math"]
y_2 = students["physics"]
plt.bar(x, y_1, label='math', color='r', alpha=0.5)
plt.bar(x, y_2, label='physics', bottom=y_1, color='b', alpha=0.5)
plt.xlabel('Студент группы')
plt.ylabel('Оценка')
plt.title('Результаты сдачи зачетов')
plt.legend()
plt.show()
