#Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР. Радуга – США,Испания,Швеция, Австралия. Определить:1. в каких турагенствах можно приобрести туры в Японию.2. в каких турагенствах нельзя приобрести туры в ЮАР.3. полный список всех туров.
voyazh = {"Mexica", "Canada", "Israel", "Italy", "USA"}
reina = {"England", "Japan", "Canada", "SAR"}
raduga = {"USA", "Spain", "Sweden", "Australia"}

for n, t in {"voyazh": voyazh, "ReynaTour": reina, "raduga": raduga}.items():
    if "Japan" in t:
        print(n)

for n, t in {"Voyazh": voyazh, "reynatour": reina, "raduga": raduga}.items():
    if "SAR" not in t:
        print(n)

print(voyazh | reina | raduga)
