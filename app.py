import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Welcome to my dashboard!")
st.checkbox('Click here to start') #allows user to interact with a checkbox
#add preview
df = pd.read_csv("Licensed_Drivers.csv")
st.write("First few rows:")
st.dataframe(df.head())

st.subheader("Total Licensed Drivers by Age Group (2015-2017)")


