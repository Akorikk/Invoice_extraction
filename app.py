import streamlit as st
import sqlite3
import pandas as pd

st.title("📊 Invoice Analytics Dashboard")

conn = sqlite3.connect("output/database.sqlite")

st.subheader("Total Spend by Vendor")
df = pd.read_sql_query("""
    SELECT vendor_name, SUM(total) as total_spend
    FROM invoices
    GROUP BY vendor_name
""", conn)
st.dataframe(df)

st.subheader("Search Invoices by Date Range")
start = st.date_input("Start Date")
end = st.date_input("End Date")

if st.button("Search"):
    df2 = pd.read_sql_query(f"""
        SELECT * FROM invoices
        WHERE date BETWEEN '{start}' AND '{end}'
    """, conn)
    st.dataframe(df2)
