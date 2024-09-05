import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

plt.plot(ypoints, linestyle = 'dashed', linewidth = '20.5')
plt.show()

plt.plot(ypoints, ls = '-.')
plt.show()

plt.plot(ypoints, color = 'r')
plt.show()