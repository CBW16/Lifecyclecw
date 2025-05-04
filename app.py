import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("Licensed Drivers in the US Dashboard")
st.checkbox('Click here to start') #allows user to interact with a checkbox *delete if unused

df = pd.read_csv("Licensed_Drivers.csv")
df = df.drop(columns=[col for col in df.columns if "Unnamed" in col])#removing unamed columns from preview

with st.expander("Data Preview"): #preview of data for user
    st.dataframe(df)

st.subheader("Total Licensed Drivers by Age Group (2015-2017)")
#1 Horizontal bar chart 
drivers_by_year = df.groupby("Year")["Drivers"].sum() / 1e6 #total drivers count for each year and adjusts the x-axis scale to not show 1e 
drivers_by_cohort = df.groupby("Cohort")["Drivers"].sum().sort_values(ascending=False) / 1e6 
#adds up every driver count in each age group

fig, ax = plt.subplots(figsize=(10, 7)) #change to find optimal size
sns.barplot(x=drivers_by_cohort.values, y=drivers_by_cohort.index, palette="Greens_d", ax=ax)
ax.set_xlabel("Number of Drivers(Millions)") 
ax.set_ylabel("Age Group")
st.pyplot(fig)

st.title("Total Drivers by State")
#2 Bar chart     save best for last?
nan_data = df[df['Year'].isna() | df['Drivers'].isna()]#nan values check
print(nan_data)

dfstate = df[['Year', 'State', 'Drivers']].dropna().astype({'Year': 'int', 'Drivers': 'int'}) #ensure correct types especially for year.Also removing my nan values

year = st.slider(  #allows user to select a year using a slider
    "Select a Year",
    min_value=int(df.Year.min()),
    max_value=int(df.Year.max()),
    value=int(df.Year.min())
)

df_year = df[df.Year == year]
by_state = df_year.groupby('State')['Drivers'].sum()

st.subheader(f"Licensed Drivers in {year}:") #shows updated chart as soon as user uses the slider
st.bar_chart(by_state)

st.title("Drivers by Sex and Year")
#3 Side by side bar chart  adjust previous df
fig = px.bar(
   df.groupby(['Year', 'Sex'], as_index=False).sum(),
   x='Year',
   y='Drivers',
   color='Sex',
   color_discrete_map={'Male': 'light blue', 'Female': 'pink'},#find perfect blue
   barmode='group',
   height=400
)
st.plotly_chart(fig, use_container_width=True)

st.title("")
#4 Pie chart? 


