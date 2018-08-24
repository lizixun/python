import matplotlib.pyplot as plt

x = list(range(1, 1001))
y = [x ** 2 for x in x]
plt.scatter(x, y, c=y, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.title("Square Numbers")
plt.xlabel("Value")
plt.ylabel("Square of Value")
plt.tick_params(axis='both', which='major')
plt.axis([0, 1100, 0, 1100000])
#plt.savefig('squares_scatter.png', bbox_inches='tight')
plt.show()