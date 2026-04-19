import matplotlib.pyplot as plt

catg = ['Apple', 'Banana', 'Orange', 'Grapes']
val = [20, 35, 30, 10]

colors = [(1,0,0), (1,1,0), (0,0,0), (1,0,1)]
plt.bar(catg, val, color = colors)

plt.xlabel("Numbers")
plt.ylabel("Fruit")
plt.title("Fruits Demand")

plt.show()