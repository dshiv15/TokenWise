import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import json
import os

st.title("TokenWise: Solana Wallet Intelligence")

# Connect to SQLite database
conn = sqlite3.connect("../backend/tokenwise.db")
st.sidebar.header("Filters")
days = st.sidebar.slider("Select time range (days)", 1, 30, 7)
start_time = (datetime.now() - timedelta(days=days)).isoformat()
end_time = datetime.now().isoformat()

# Fetch data
query = f"SELECT * FROM transactions WHERE timestamp BETWEEN ? AND ?"
df = pd.read_sql_query(query, conn, params=(start_time, end_time))
holders = pd.read_sql_query("SELECT * FROM holders", conn)

# Dashboard components
st.header("Market Trends")
buys = len(df[df["isBuy"] == 1])
sells = len(df[df["isBuy"] == 0])
net_direction = "Buy-Heavy" if buys > sells else "Sell-Heavy"
st.metric("Total Buys", buys)
st.metric("Total Sells", sells)
st.metric("Net Direction", net_direction)

# Protocol usage
protocol_counts = df["protocol"].value_counts().reset_index()
fig = px.pie(protocol_counts, values="count", names="protocol", title="Protocol Usage")
st.plotly_chart(fig)

# Repeated activity
wallet_activity = df["wallet"].value_counts().head(10).reset_index()
fig2 = px.bar(wallet_activity, x="wallet", y="count", title="Top Active Wallets")
st.plotly_chart(fig2)

# Export data
if st.button("Export Transactions as CSV"):
    df.to_csv("../data/transactions.csv", index=False)
    st.success("Exported to data/transactions.csv")
if st.button("Export Transactions as JSON"):
    df.to_json("../data/transactions.json", orient="records", indent=2)
    st.success("Exported to data/transactions.json")

conn.close()
