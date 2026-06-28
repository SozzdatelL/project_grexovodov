#Приложение РАСПРЕДЕЛЕНИЕ ДОПОЛНИТЕЛЬНЫХ ОБЯЗАННОСТЕЙ для некоторой организации. БД должна содержать таблицу Обязанности со следующей структурой записи: ФИО работника, вид дополнительной работы, сумма оплаты, срок.

import sqlite3 as sq

duties_data = [
    ('Смирнов А.В.', 'Подготовка внутренней документации', 6500.00, '2026-10-15'),
    ('Орлова Н.П.', 'Организация обучения персонала', 9500.00, '2026-11-20'),
    ('Захаров Д.С.', 'Контроль пожарной безопасности', 12500.00, '2027-02-10'),
    ('Лебедева И.К.', 'Организация корпоративных встреч', 7000.00, '2026-09-25'),
    ('Егоров М.А.', 'Администрирование корпоративного портала', 11000.00, '2026-12-05'),
    ('Крылова О.В.', 'Координация логистики', 8000.00, '2026-08-30'),
    ('Тарасов П.Н.', 'Проведение инструктажей', 9000.00, '2027-04-18'),
    ('Виноградова Е.А.', 'Ведение электронного архива', 4800.00, '2026-07-28'),
    ('Соколов И.В.', 'Мониторинг IT-оборудования', 13000.00, '2026-12-12'),
    ('Белова К.С.', 'Подготовка аналитических отчетов', 14500.00, '2027-03-15')
]


with sq.connect('duties.db') as con:
    cursor = con.cursor()

    cursor.execute("DROP TABLE IF EXISTS Обязанности")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Обязанности (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio TEXT NOT NULL,
        work_type TEXT NOT NULL,
        payment REAL NOT NULL,
        deadline TEXT NOT NULL
    )
    """)

    cursor.executemany(
        """
        INSERT INTO Обязанности
        VALUES (NULL, ?, ?, ?, ?)
        """,
        duties_data
    )

    def print_table(title):
        print("\n" + title)
        print("-" * 95)
        print(
            f"{'ID':<4}"
            f"{'ФИО работника':<30}"
            f"{'Вид работы':<40}"
            f"{'Оплата':<12}"
            f"{'Срок'}"
        )

        cursor.execute("SELECT * FROM Обязанности ORDER BY id")

        for row in cursor.fetchall():
            id_, fio, work, pay, dead = row
            print(
                f"{id_:<4}"
                f"{fio:<30}"
                f"{work:<40}"
                f"{pay:<12.2f}"
                f"{dead}"
            )

    print_table("Исходное содержимое таблицы")

    print("\n1. Работники с оплатой более 10000:")

    cursor.execute("""
        SELECT fio, work_type, payment
        FROM Обязанности
        WHERE payment > 10000
    """)

    for fio, work, pay in cursor.fetchall():
        print(f" - {fio} ({work}) — {pay:.2f} руб.")

    print("\n2. Работники со сроком выполнения в 2027 году:")

    cursor.execute("""
        SELECT fio, deadline
        FROM Обязанности
        WHERE deadline LIKE '2027%'
    """)

    for fio, dead in cursor.fetchall():
        print(f" - {fio} (срок: {dead})")

    print("\n3. Работники, чья работа связана с IT или порталом:")

    cursor.execute("""
        SELECT fio, work_type
        FROM Обязанности
        WHERE work_type LIKE '%IT%'
        OR work_type LIKE '%портал%'
    """)

    for fio, work in cursor.fetchall():
        print(f" - {fio} ({work})")

    cursor.execute("""
        UPDATE Обязанности
        SET payment = 15000
        WHERE work_type = 'Мониторинг IT-оборудования'
    """)

    cursor.execute("""
        UPDATE Обязанности
        SET deadline = '2027-06-01'
        WHERE fio LIKE '%Смирнов%'
    """)

    cursor.execute("""
        UPDATE Обязанности
        SET work_type = 'Координация логистики и склада'
        WHERE fio LIKE '%Крылова%'
    """)

    print_table("Таблица после редактирования")

    cursor.execute("""
        DELETE FROM Обязанности
        WHERE fio LIKE '%Тарасов%'
    """)

    cursor.execute("""
        DELETE FROM Обязанности
        WHERE id = 8
    """)

    cursor.execute("""
        DELETE FROM Обязанности
        WHERE payment <= 5000
    """)

    print_table("Итоговая таблица после удаления")

    con.commit()
