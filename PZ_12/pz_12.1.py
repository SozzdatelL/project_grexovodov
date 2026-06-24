matrix = [
    [1, -2, 3],
    [4, 5, -6],
    [7, 8, 9],
    [-1, 2, -3]
]

replacement_array = [10, 20, 30]

print("Исходная матрица:")
for row in matrix:
    print(row)

# 1. Замена 3-й строки
matrix[2] = replacement_array

print("\nМатрица после замены 3-й строки:")
for row in matrix:
    print(row)

# 2. Среднее арифметическое положительных элементов
total = 0
count = 0

for row in matrix:
    for element in row:
        if element > 0:
            total += element
            count += 1

if count > 0:
    average = total / count
else:
    average = 0

print("\nСреднее арифметическое положительных элементов:", average)
