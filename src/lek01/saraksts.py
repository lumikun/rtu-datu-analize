import statistics

arr = [3, 1, 5, 6, 7, 8, 9, 8, 2, 1, 4]
print(arr)
print(sum(arr))
print(sum(arr)/len(arr))
print(min(arr))
print(max(arr))
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)
arr.append(10)
print(arr)
median = statistics.median(arr)
print(median)

with open("dati.txt", mode="r", encoding="utf-8") as f:
    array = f.readlines()

l = []
for n in array:
    l.append(int(n.rstrip()))
    print(n.rstirp())

print(sum(l))

