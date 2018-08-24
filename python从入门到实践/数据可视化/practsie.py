import matplotlib.pyplot as plt

x = list(range(1, 5000))
y = [x ** 3 for x in x]
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=x^3")
plt.scatter(x, y, c=y, cmap=plt.cm.Greens, s=40)
plt.axis([0, 5100, 0, 5100 ** 3])
plt.show()
