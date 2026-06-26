#2. Дан список размера N. Найти количество его промежутков монотонности (то есть участков, на которых его элементы возрастают или убывают).

N = int(input())
A = list(map(int, input().split()))

if N <= 1:
    print(0)
else:
    count = 1

    i = 1
    while i < N and A[i] == A[i - 1]:
        i += 1

    if i == N:
        print(1)
    else:
        direction = 1 if A[i] > A[i - 1] else -1

        for j in range(i + 1, N):
            if A[j] > A[j - 1]:
                new_dir = 1
            elif A[j] < A[j - 1]:
                new_dir = -1
            else:
                continue

            if new_dir != direction:
                count += 1
                direction = new_dir

        print(count)
