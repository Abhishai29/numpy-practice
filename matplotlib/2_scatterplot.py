import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = np.sin(x)

plt.scatter(x, y, color = 'red', marker = 'o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter plot of Sine Function")

plt.show()