#1. Проверьте наличие значения 200 в sample_dict = {'a': 100, 'b': 200, 'c': 300}.

sample_dict = {'a': 100, 'b': 200, 'c': 300}

found = False

for value in sample_dict.values():
    if value == 200:
        found = True
        break

if found:
    print("Значение 200 найдено")
else:
    print("Значение 200 не найдено")
