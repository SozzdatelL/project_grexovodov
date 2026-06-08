def task2(A):
    if len(A) < 2: return 0
    cnt = 1
    for i in range(1, len(A)-1):
        if (A[i]-A[i-1]) * (A[i+1]-A[i]) < 0:
            cnt += 1
    return cnt

A = [1, 3, 5, 4, 2, 7, 8]
print(task2(A))
