#В исходном текстовом файле (Dostoevsky.txt) найти все фамилии с инициалами (например, А. Ф. Куманиной и т.п.).

import re
with open('/home/workdir/attachments/Dostoevsky.txt', 'r', encoding='utf-8') as f:
    text = f.read()
matches = re.findall(r'\b([А-ЯЁ]\.\s*[А-ЯЁ]\.?\s*[А-ЯЁ][а-яё]*)\b', text)
print(matches)
