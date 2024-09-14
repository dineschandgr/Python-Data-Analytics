import plotly.express as px
import pandas as pd

# using the iris dataset

df = px.data.iris()

# plotting the line chart
fig = px.line(df, y="sepal_width",)

# showing the plot
fig.show()

# using the iris dataset
df = pd.read_csv('iris.csv')

# plotting the line chart
fig = px.line(df, y="SepalLengthCm", line_dash='Species',
              color='Species')

# showing the plot
fig.show()