#Дан список A размера N и целое число K (1 < K < N). Вывести элементы список с порядковыми номерами, кратными K: AK, A2*K, A3*K,... . Условный оператор не использовать.

N = int(input())
A = list(map(int, input().split()))
K = int(input())

for i in range(K - 1, N, K):
    print(A[i])
    
