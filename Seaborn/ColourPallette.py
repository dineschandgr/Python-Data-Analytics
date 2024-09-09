# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# current colot palette
palette = sns.color_palette()

# plots the color palette as a
# horizontal array
sns.palplot(palette)

plt.show()

palette = sns.color_palette('PiYG', 11)

# diverging color palette
sns.palplot(palette)
plt.show()

palette = sns.color_palette('Greens', 11)

# sequential color palette
sns.palplot(palette)

plt.show()