#Создать txt → записать количество, элементы в обратном порядке и сумму второй половины


f = open("numbers.txt", "w")

a = list(map(int, input("Введите числа: ").split()))

f.write("Исходные данные:\n")
f.write(" ".join(map(str, a)) + "\n")

f.write("Количество элементов:\n")
f.write(str(len(a)) + "\n")

f.write("Элементы в обратном порядке:\n")
f.write(" ".join(map(str, a[::-1])) + "\n")

f.write("Сумма элементов последней половины:\n")
f.write(str(sum(a[len(a)//2:])))

f.close()

