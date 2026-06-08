#Дано целое число N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2N)2
n = int(input())

s = 0

for i in range(n, 2 * n + 1):
    s = s + i * i

print(s)
