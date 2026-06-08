def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

N = int(input())

count = 0
while N > 0:
    N -= sum_digits(N)
    count += 1

print(count)
