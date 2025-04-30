import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
st.header("This is a header")
st.subheader("This is a subheader")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120)
date = st.date_input("Select a date")

if name:
    st.write(f"Hello {name}! You are {age} years old.")

df = pd.DataFrame({
    'A': np.random.randn(10),
    'B': np.random.randn(10)
})
df  