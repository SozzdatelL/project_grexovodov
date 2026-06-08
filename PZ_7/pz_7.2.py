path = input()
parts = path.split("\\")

if len(parts) <= 2:
    print("\\")
else:
    print(parts[-2])
