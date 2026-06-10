#Приложение ПРОМЫШЛЕННОСТЬ для автоматизированного учета информации о промышленных предприятиях республики. БД содержит таблицу Предприятия, имеющую следующую структуру записи: Код предприятия, Наименование предприятия, Физический адрес, Филиалы (количество филиалов), Общая числ, персонала, Общая стоим оборудования, Объем выпускаемой продукции, Дата регистрации.

import sqlite3

conn = sqlite3.connect('industry.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Predpriyatiya (
    kod INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    filials INTEGER,
    personnel INTEGER,
    equipment REAL,
    volume REAL,
    reg_date TEXT
)''')

for _ in range(10):
    data = (
        int(input("Код: ")),
        input("Наименование: "),
        input("Адрес: "),
        int(input("Филиалы: ")),
        int(input("Персонал: ")),
        float(input("Стоим. оборудования: ")),
        float(input("Объем продукции: ")),
        input("Дата регистрации: ")
    )
    c.execute("INSERT INTO Predpriyatiya VALUES (?,?,?,?,?,?,?,?)", data)

conn.commit()

def menu():
    print("1. Поиск 2. Удаление 3. Редактирование 4. Выход")
    return input("Выбор: ")

def search():
    print("1. По коду 2. По названию 3. По адресу")
    ch = input()
    if ch == '1': q = "SELECT * FROM Predpriyatiya WHERE kod=?"
    elif ch == '2': q = "SELECT * FROM Predpriyatiya WHERE name LIKE ?"
    else: q = "SELECT * FROM Predpriyatiya WHERE address LIKE ?"
    val = input("Значение: ")
    for row in c.execute(q, (val if ch=='1' else f"%{val}%",)): print(row)


def delete():
    print("1. По коду 2. По названию 3. По адресу")
    ch = input()
    if ch == '1': q = "DELETE FROM Predpriyatiya WHERE kod=?"
    elif ch == '2': q = "DELETE FROM Predpriyatiya WHERE name LIKE ?"
    else: q = "DELETE FROM Predpriyatiya WHERE address LIKE ?"
    val = input("Значение: ")
    c.execute(q, (val if ch=='1' else f"%{val}%",))
    conn.commit()


def edit():
    print("1. По коду 2. По названию 3. По адресу")
    ch = input()
    if ch == '1': cond = "kod=?"
    elif ch == '2': cond = "name LIKE ?"
    else: cond = "address LIKE ?"
    val = input("Условие: ")
    field = input("Поле (name/address/filials/personnel/equipment/volume/reg_date): ")
    newval = input("Новое значение: ")
    c.execute(f"UPDATE Predpriyatiya SET {field}=? WHERE {cond}", (newval, val if ch=='1' else f"%{val}%"))
    conn.commit()

while True:
    choice = menu()
    if choice == '1': search()
    elif choice == '2': delete()
    elif choice == '3': edit()
    elif choice == '4': break

conn.close()
