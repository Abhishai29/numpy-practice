import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10)
y = np.random.rand(10)

colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue','purple', 'pink', 'white']
plt.scatter(x, y, c = colors, s = 100)
# s = 100 increases marker size

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter plot with Different colors")

plt.show()