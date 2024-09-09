# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import set_context

data = sns.load_dataset("iris")

def graph():
	sns.lineplot(x="sepal_length", y="sepal_width", data=data)
	set_context(context=None, font_scale=1, rc=None)
	sns.set_context("paper")


# Creating a new figure with width = 5 inches
# and height = 4 inches
fig = plt.figure(figsize =(5, 4))

# Creating first axes for the figure
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# plotting the graph
graph()

# Creating second axes for the figure
ax2 = fig.add_axes([0.5, 0.5, 0.3, 0.3])

# plotting the graph
graph()

plt.show()
