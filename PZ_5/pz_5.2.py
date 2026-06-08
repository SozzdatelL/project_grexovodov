#Описать функцию Minmax(X, Y), записывающую в переменную X минимальное из значений X и Y, а в переменную Y — максимальное из этих значений (X и Y — вещественные параметры, являющиеся одновременно входными и выходными). Используя четыре вызова этой функции, найти минимальное и максимальное изданных чисел A, B, C, D.
def Minmax(x, y):
    if x > y:
        x, y = y, x
    return x, y

A = float(input())
B = float(input())
C = float(input())
D = float(input())

A, B = Minmax(A, B)
C, D = Minmax(C, D)
A, C = Minmax(A, C)
B, D = Minmax(B, D)

print("Минимум:", A)
print("Максимум:", D)
