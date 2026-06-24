#В исходном текстовом файле (Dostoevsky.txt) найти все фамилии с инициалами (например, А. Ф. Куманиной и т.п.).

import re

with open("Dostoevsky.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"[А-ЯЁ]\.\s?[А-ЯЁ]\.\s?[А-Яа-яЁё]+"

matches = re.findall(pattern, text)

print("Найденные фамилии с инициалами:\n")

for name in matches:
    print(name)
