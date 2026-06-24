#Приложение ПРОМЫШЛЕННОСТЬ для автоматизированного учета информации о промышленных предприятиях республики. БД содержит таблицу Предприятия, имеющую следующую структуру записи: Код предприятия, Наименование предприятия, Физический адрес, Филиалы (количество филиалов), Общая числ, персонала, Общая стоим оборудования, Объем выпускаемой продукции, Дата регистрации.

import sqlite3

conn = sqlite3.connect("industry.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS enterprises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    branches INTEGER,
    staff INTEGER,
    equipment_cost REAL,
    production_volume REAL,
    registration_date TEXT
)
""")

conn.commit()

def add_enterprise(name, address, branches, staff, equipment_cost, production_volume, registration_date):
    cursor.execute("""
    INSERT INTO enterprises (
        name, address, branches, staff,
        equipment_cost, production_volume, registration_date
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, address, branches, staff, equipment_cost, production_volume, registration_date))

    conn.commit()


def show_enterprises():
    cursor.execute("SELECT * FROM enterprises")
    rows = cursor.fetchall()

    print("\nСписок предприятий:")
    for row in rows:
        print(row)

add_enterprise(
    "Завод Прогресс",
    "г. Минск, ул. Ленина 10",
    3,
    1200,
    5000000,
    250000,
    "2010-05-12"
)

add_enterprise(
    "МеталлПром",
    "г. Гомель, ул. Заводская 5",
    2,
    800,
    3200000,
    180000,
    "2015-09-20"
)

show_enterprises()

conn.close()
