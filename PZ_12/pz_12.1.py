#заменить элементы 3 строки матрицы элементами из одномерного динамического массива

n = int(input('strokes: '))
m = int(input('stolbcov: '))

a = [list(map(int, input().split())) for i in range(n)]

b = list(map(int, input('new massive: ').split()))

a[2] = b

for i in a:
    print(i)
