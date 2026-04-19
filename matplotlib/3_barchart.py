import matplotlib.pyplot as plt

catg = ["A", "B", "C", "D"]
val = [4, 7, 1, 8]

plt.bar(catg, val, color = 'blue')

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart eg.")

plt.show()

