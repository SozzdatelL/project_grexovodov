#В последовательности на n целых чисел найти и вынести: макс. среди отриц.элементы кратные двум и их сумму.

a = [5, -2, 8, -1, 3, 7, -10, 4, -6]

neg_max = max((x for x in a if x < 0), default="no")
evens = [x for x in a if x % 2 == 0]
print(neg_max)
print(evens)
print(sum(evens))
