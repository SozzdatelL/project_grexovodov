#https://professorweb.ru/my/html/html5/level2/files/img46023.jpgfrom tkinter import *

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def submit_form():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    age = entry_age.get()
    gender = gender_var.get()
    qualities = text_qualities.get("1.0", END).strip()

    selected_animals = [
        animal
        for animal, var in animal_vars.items()
        if var.get()
    ]

    if not name or not phone:
        messagebox.showwarning(
            "Ошибка",
            "Заполните имя и телефон"
        )
        return

    result = f"""
Имя: {name}
Телефон: {phone}
Email: {email}

Возраст: {age}
Пол: {gender}

Качества:
{qualities}

Любимые животные:
{", ".join(selected_animals)}
"""

    messagebox.showinfo(
        "Форма отправлена",
        result
    )


root = Tk()
root.title("Форма записи на работу в зоопарк")
root.geometry("600x750")
root.configure(bg="#f0f0f0")


Label(
    root,
    text="Форма записи на работу в зоопарк",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0"
).grid(
    row=0,
    column=0,
    columnspan=2,
    pady=(15, 5)
)

Label(
    root,
    text="Пожалуйста, заполните форму. Обязательные поля помечены *",
    font=("Arial", 9),
    bg="#f0f0f0"
).grid(
    row=1,
    column=0,
    columnspan=2,
    pady=(0, 15)
)


frame_contact = LabelFrame(
    root,
    text="Контактная информация",
    font=("Arial", 10, "bold")
)
frame_contact.grid(
    row=2,
    column=0,
    columnspan=2,
    sticky="ew",
    padx=20,
    pady=5
)

Label(frame_contact, text="Имя *").grid(row=0, column=0, sticky="w")
entry_name = Entry(frame_contact, width=40)
entry_name.grid(row=0, column=1, pady=5, padx=10)

Label(frame_contact, text="Телефон *").grid(row=1, column=0, sticky="w")
entry_phone = Entry(frame_contact, width=40)
entry_phone.grid(row=1, column=1, pady=5, padx=10)

Label(frame_contact, text="Email").grid(row=2, column=0, sticky="w")
entry_email = Entry(frame_contact, width=40)
entry_email.grid(row=2, column=1, pady=5, padx=10)


frame_personal = LabelFrame(
    root,
    text="Персональная информация",
    font=("Arial", 10, "bold")
)
frame_personal.grid(
    row=3,
    column=0,
    columnspan=2,
    sticky="ew",
    padx=20,
    pady=10
)

Label(frame_personal, text="Возраст").grid(
    row=0,
    column=0,
    sticky="w"
)

entry_age = Entry(frame_personal, width=20)
entry_age.grid(
    row=0,
    column=1,
    sticky="w",
    padx=10,
    pady=5
)

Label(frame_personal, text="Пол").grid(
    row=1,
    column=0,
    sticky="w"
)

gender_var = StringVar(value="Мужской")

gender_combo = ttk.Combobox(
    frame_personal,
    textvariable=gender_var,
    values=["Мужской", "Женский"],
    state="readonly",
    width=18
)

gender_combo.grid(
    row=1,
    column=1,
    sticky="w",
    padx=10,
    pady=5
)

Label(
    frame_personal,
    text="Перечислите свои личные качества:"
).grid(
    row=2,
    column=0,
    sticky="nw"
)

text_qualities = Text(
    frame_personal,
    width=40,
    height=5
)

text_qualities.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


frame_animals = LabelFrame(
    root,
    text="Выберите любимых животных",
    font=("Arial", 10, "bold")
)

frame_animals.grid(
    row=4,
    column=0,
    columnspan=2,
    sticky="ew",
    padx=20,
    pady=10
)

animals = [
    "Зебра",
    "Кот",
    "Анаконда",
    "Питон",
    "Слон",
    "Антилопа",
    "Орёл",
    "Краб"
]

animal_vars = {}

for i, animal in enumerate(animals):
    animal_vars[animal] = BooleanVar()

    Checkbutton(
        frame_animals,
        text=animal,
        variable=animal_vars[animal]
    ).grid(
        row=i // 4,
        column=i % 4,
        padx=10,
        pady=5,
        sticky="w"
    )


Button(
    root,
    text="Отправить информацию",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    command=submit_form
).grid(
    row=5,
    column=0,
    columnspan=2,
    pady=20
)

root.mainloop()
