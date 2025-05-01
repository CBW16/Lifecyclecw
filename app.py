import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Licensed Drivers in the US Dashboard")
st.checkbox('Click here to start') #allows user to interact with a checkbox

df = pd.read_csv("Licensed_Drivers.csv")

with st.expander("Data Preview"): #preview of data for user
    st.dataframe(df.head())

st.subheader("Total Licensed Drivers by Age Group (2015-2017)")


