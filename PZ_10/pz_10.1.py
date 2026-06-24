#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов: 
#Исходные данные:
#Количество элементов:
#Элементы в обратном порядке:
#Сумма элементов последней половины:


numbers = [12, -3, 7, -8, 5, 10, -2, 4]

with open("input.txt", "w", encoding="utf-8") as file:
    file.write(" ".join(map(str, numbers)))

with open("input.txt", "r", encoding="utf-8") as file:
    data = list(map(int, file.read().split()))

count = len(data)
reversed_data = data[::-1]
second_half_sum = sum(data[len(data)//2:])

with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Исходные данные: " + " ".join(map(str, data)) + "\n")
    file.write("Количество элементов: " + str(count) + "\n")
    file.write("Элементы в обратном порядке: " + " ".join(map(str, reversed_data)) + "\n")
    file.write("Сумма элементов последней половины: " + str(second_half_sum) + "\n")
