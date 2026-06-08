#В матрице найти среднее арифм. положительных элементов.
positives = [x for row in matrix for x in row if x > 0]
print(sum(positives) / len(positives) if positives else 0)
