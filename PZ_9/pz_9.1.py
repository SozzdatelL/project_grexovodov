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
