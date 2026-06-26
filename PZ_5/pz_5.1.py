#Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму его цифр и т. д. Через сколько таких действий получится нуль?

def digit_sum(n):
    return sum(int(d) for d in str(n))

def steps_to_zero(n):
    steps = 0
    
    while n > 0:
        n -= digit_sum(n)
        steps += 1
    
    return steps

n = int(input())
print(steps_to_zero(n))
