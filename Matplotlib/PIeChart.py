import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

data = [35, 25, 25, 15]

plt.pie(data, y)
plt.show()

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(data, y, labels = mylabels)
plt.show()

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()
