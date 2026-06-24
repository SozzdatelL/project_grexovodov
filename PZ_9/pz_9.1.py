#Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР. Радуга – США,Испания,Швеция, Австралия. Определить:1. в каких турагенствах можно приобрести туры в Японию.2. в каких турагенствах нельзя приобрести туры в ЮАР.3. полный список всех туров.

agencies = {
    "Вояж": ["Мексика", "Канада", "Израиль", "Италия", "США"],
    "РейнаТур": ["Англия", "Япония", "Канада", "ЮАР"],
    "Радуга": ["США", "Испания", "Швеция", "Австралия"]
}

japan_tours = []

for agency, countries in agencies.items():
    if "Япония" in countries:
        japan_tours.append(agency)

print("1. Туры в Японию можно приобрести в:")
print(", ".join(japan_tours))

not_south_africa = []

for agency, countries in agencies.items():
    if "ЮАР" not in countries:
        not_south_africa.append(agency)

print("\n2. Туры в ЮАР нельзя приобрести в:")
print(", ".join(not_south_africa))

all_tours = set()

for countries in agencies.values():
    all_tours.update(countries)

print("\n3. Полный список всех туров:")
print(", ".join(sorted(all_tours)))
