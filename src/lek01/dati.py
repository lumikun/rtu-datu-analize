with open("bigdati.csv", "r") as f:
    lines = f.readlines()


arr = []

for line in lines:
    row = line.rstrip().split(",")
    try:
        arr.append(float(row[5]))
    except ValueError: 
        arr.append(0)
        pass

print(len(arr))
print(max(arr))
print(min(arr))
print(sum(arr)/len(arr))
print(sum(arr))
