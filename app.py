import plotly.express as px
import streamlit as st
import time
import numpy as np
from iris.data import get_iris_data

st.title("Plotting demo")
st.markdown("Demonstration of Streamlit")

# Filtering dataset
st.sidebar.title("Sidebar")
radio = st.sidebar.radio("Species", options=['setosa', 'virginica', 'versicolor'])
df = get_iris_data()
fig = px.scatter(df[df.species == radio], x="sepal_width", y="sepal_length", color="species")

st.sidebar.title("Progress")
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)

st.markdown("Iris Plot")
iris_plot = st.plotly_chart(fig)

st.markdown("Progress Plot")
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Completed" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()
