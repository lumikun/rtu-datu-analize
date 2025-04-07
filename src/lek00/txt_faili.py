# STUB
with open("texts.txt", mode="r", encoding="utf-8") as data:

with open("result.csv", mode="w", encoding="utf-8") as datne:
    datne.write("Janis,10,10,100\n")
    datne.write("Peteris,20,10,200\n")

with open("result.csv", mode="a", encoding="utf-8") as datne:
    datne.write("Girts,10,10,100\n")
    datne.write("Zanis,20,10,200\n")
