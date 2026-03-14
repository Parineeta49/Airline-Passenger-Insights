import streamlit as st
import pandas as pd

st.title("✈️ Global Airline Passenger Dashboard")

df = pd.read_csv("../data/airline_passenger_data.csv")

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Flight Status Distribution")
status = df["Flight Status"].value_counts()
st.bar_chart(status)

st.subheader("Passenger Age Distribution")
st.line_chart(df["Age"])