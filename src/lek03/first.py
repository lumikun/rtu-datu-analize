import matplotlib.pyplot as plt

x = list(range(1,11))
y = [1, 4, 2, 5, 3, 7, 9, 19, 90, 10]

# plt.bar(x, y)
# plt.savefig("Bar.png")
# plt.barh(x,y)
# plt.show()

# plt.plot(x, y, marker="x")
# plt.show()

y2 = [i**2 for i in x] # Saisinatais cikls/list comprehension.
# [i**2 for i in x if x%2==0]
# plt.plot(x, y, "o-b")
# plt.plot(x, y2, "^--r")
# plt.show()

# plt.pie(y, labels=x, autopct="%.1f%%")
# plt.title("Grafiks")
# plt.show()

