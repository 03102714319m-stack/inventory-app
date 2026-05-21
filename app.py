import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inventory Dashboard", layout="wide")

st.title("📦 Inventory + Sales Dashboard")

# -------------------------
# Upload Files
# -------------------------
inventory_file = st.file_uploader("📦 Upload Inventory File (Excel)")
sales_file = st.file_uploader("📊 Upload Sales File (Excel)")

if inventory_file and sales_file:

    inventory = pd.read_excel(inventory_file)
    sales = pd.read_excel(sales_file)

    st.success("Files uploaded successfully ✅")

    # -------------------------
    # DASHBOARD METRICS
    # -------------------------
    col1, col2 = st.columns(2)

    col1.metric("📦 Inventory Items", len(inventory))
    col2.metric("📊 Sales Records", len(sales))

    st.divider()

    # -------------------------
    # SHOW DATA
    # -------------------------
    st.subheader("📦 Inventory Data")
    st.dataframe(inventory)

    st.subheader("📊 Sales Data")
    st.dataframe(sales)

    # -------------------------
    # SEARCH
    # -------------------------
    st.subheader("🔍 Search Product")

    product = st.text_input("Enter product name")

    if product:
        result = sales[sales["Product"].astype(str).str.contains(product, case=False, na=False)]
        st.dataframe(result)

    # -------------------------
    # SIMPLE CHART
    # -------------------------
    st.subheader("📈 Sales Chart")

    if "Quantity" in sales.columns:
        chart_data = sales.groupby("Product")["Quantity"].sum()
        st.bar_chart(chart_data)

    # -------------------------
    # DOWNLOAD
    # -------------------------
    csv = sales.to_csv(index=False)

    st.download_button(
        "⬇ Download Report",
        csv,
        "sales_report.csv",
        "text/csv"
    )

else:
    st.info("📌 Please upload Inventory + Sales files")