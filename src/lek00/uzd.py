
b = int(input("Bernu skaits?: "))
avenes = float(input("Avenu skaits litros?: "))
with open("avenes.csv", mode="a", encoding="utf-8") as data:
    data.write(f"{b},{avenes},{b*avenes}\n")

