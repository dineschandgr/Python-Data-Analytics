import streamlit as st
import pandas as pd
import numpy as np

st.title("Simple Streamlit App")
st.write("This is an example of a Streamlit app.")

# Create a slider
x = st.slider("Select a value for x", 0, 100, 50)
st.write(f"You selected {x}!")

# Plot a random chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)
