#Вывести файл, посчитать заглавные буквы, создать новый файл с автором и названием

f = open("text18-10.txt", "r", encoding="utf-8")

text = f.read()
print(text)

k = 0
for i in text:
    if i.isupper():
        k += 1

print("Количество больших букв:", k)

new = open("new_text.txt", "w", encoding="utf-8")

new.write(text)
new.write("\n\nАвтор: М. Ю. Лермонтов")
new.write("\nНазвание: Бородино")

f.close()
new.close()
