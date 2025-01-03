import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

st.title("Streamlit charts")

st.subheader("Once the data is present, charts are easy to create using prebuilt attributes")
st.divider()

st.subheader("Sample Data")
data = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])
st.write(data)
st.divider()

st.subheader("Area Chart")
st.area_chart(data)
st.divider()

st.subheader("Bar Chart")
st.bar_chart(data)
st.divider()

st.subheader("Line Chart")
st.line_chart(data)
st.divider()

st.subheader("Scatter Chart")
st.scatter_chart(data)
st.divider()

st.subheader("Scatter Chart")
st.scatter_chart(pd.DataFrame({"x": np.random.randn(100), "y": np.random.randn(100), "z": np.random.randn(100), "k": np.random.randn(100)}))
st.divider()

st.subheader("Map")
st.map(pd.DataFrame(np.random.randn(100,2)/[50,50] + [15.9129, 79.7400], columns=['lat', 'lon']))
st.divider()