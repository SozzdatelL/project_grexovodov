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
