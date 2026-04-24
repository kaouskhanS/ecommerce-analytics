import streamlit as st
import pandas as pd

df = pd.read_csv("../data/ecommerce_data.csv")

st.title("E-Commerce Analytics Dashboard")

st.metric("Total Revenue", int(df["revenue"].sum()))
st.metric("Avg Order Value", int(df["revenue"].mean()))

st.bar_chart(df.groupby("category")["revenue"].sum())
st.line_chart(df.groupby("order_date")["revenue"].sum())
