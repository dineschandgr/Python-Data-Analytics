# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)
plt.xlim(5)
plt.ylim(3)


plt.title('Title using Matplotlib Function')
plt.show()