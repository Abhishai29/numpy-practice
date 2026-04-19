import matplotlib.pyplot as plt

V = ['Cars', 'Bikes', 'Buses', 'Trains']
d = [30, 15, 45, 10]

plt.pie(d, autopct = '%1.1f%%', labels = V )
plt.show()