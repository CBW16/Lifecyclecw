import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Licensed Drivers in the US Dashboard")
st.checkbox('Click here to start') #allows user to interact with a checkbox

df = pd.read_csv("Licensed_Drivers.csv")
df = df.drop(columns=[col for col in df.columns if "Unnamed" in col])#removing unamed columns

with st.expander("Data Preview"): #preview of data for user
    st.dataframe(df)

st.subheader("Total Licensed Drivers by Age Group (2015-2017)")

drivers_by_year = df.groupby("Year")["Drivers"].sum() / 1e6 #total drivers count for each year 
drivers_by_cohort = df.groupby("Cohort")["Drivers"].sum().sort_values(ascending=False) / 1e6 
#adds up every driver count in each age group

fig, ax = plt.subplots(figsize=(10, 7)) #change to find optimal size
sns.barplot(x=drivers_by_cohort.values, y=drivers_by_cohort.index, palette="Greens_d", ax=ax)
ax.set_xlabel("Number of Drivers(Millions)") 
ax.set_ylabel("Age Group")
st.pyplot(fig)


st.title("Total Drivers by State")

df = df[['Year', 'State', 'Drivers']].astype({'Year': 'int', 'Drivers': 'int'}) #ensure correct types especially for year


year = st.slider(  #allows user to select a year using a slider
    "Select Year",
    min_value=int(df.Year.min()),
    max_value=int(df.Year.max()),
    value=int(df.Year.min())
)


df_year = df[df.Year == year]
by_state = df_year.groupby('State')['Drivers'].sum()

st.subheader(f"Licensed Drivers in Year") #shows updated chart as soon as user uses the slider
st.bar_chart(by_state)

