import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(-5, 5)
y = 2 * x + 3

plt.plot(x, y, linewidth = 2, color = 'grey')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line")
plt.grid(True)

plt.show()
