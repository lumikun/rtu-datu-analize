def append_to(x, y):
    try:
        x.append(int(y))
    except ValueError:
        x.append(0)
        pass

def appendstr_to(x, y):
    try:
        x.append(str(y))
    except ValueError:
        x.append("NULL")

with open("auto.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

Mark = []
year = []
fuel = []
for l in lines:
    row = l.rstrip().split(',')
    if row[1] == "VW":
        appendstr_to(Mark, row[1])
        append_to(year, row[6])
        appendstr_to(fuel ,row[4])

print(f"Latvijā ir reģistrēti {len(Mark)}, {Mark[1]} Markas auto, vecākais ir reģistrēts {max(year)} gadā.")

