import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- Load Data Function ---
@st.cache_data
def load_data():
    base_path = os.path.join("data")
    clustered = pd.read_csv(os.path.join(base_path, "KMeans_Customer_Segment_Table.csv"))
    rfm = pd.read_csv(os.path.join(base_path, "rfm_table.csv"))
    return clustered, rfm

clustered_df, rfm_df = load_data()

# --- SIDEBAR ---
st.sidebar.title("📊 RFM Segment Explorer")
view_option = st.sidebar.radio("Select Dataset View:", ["Clustered RFM", "Raw RFM"])
if view_option == "Clustered RFM":
    df = clustered_df.copy()
else:
    df = rfm_df.copy()

# Optional filters
st.sidebar.subheader("🔍 Filter Customers")
recency_range = st.sidebar.slider("Recency (days):", int(df["recency_days"].min()), int(df["recency_days"].max()), (0, 100))
frequency_range = st.sidebar.slider("Frequency:", int(df["frequency"].min()), int(df["frequency"].max()), (0, 10))
monetary_range = st.sidebar.slider("Monetary ($):", float(df["monetary"].min()), float(df["monetary"].max()), (0.0, 5000.0))

# If clustered, allow segment filtering
if "Segment_Name" in df.columns:
    segments = df["Segment_Name"].unique().tolist()
    selected_segments = st.sidebar.multiselect("Segment(s):", segments, default=segments)
    df = df[df["Segment_Name"].isin(selected_segments)]

# Apply filters
df = df[
    (df["recency_days"].between(*recency_range)) &
    (df["frequency"].between(*frequency_range)) &
    (df["monetary"].between(*monetary_range))
]

# --- MAIN UI ---
st.title("🏦 BankTrust RFM Customer Segmentation")

tab1, tab2, tab3 = st.tabs(["📈 Overview", "🧠 Segments", "🧍 Customer Explorer"])

with tab1:
    st.subheader("RFM Metrics Distribution")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", f"{len(df):,}")
    col2.metric("Avg Frequency", f"{df['frequency'].mean():.2f}")
    col3.metric("Avg Monetary ($)", f"{df['monetary'].mean():.2f}")

    st.plotly_chart(px.histogram(df, x="recency_days", nbins=30, title="Recency Distribution"))
    st.plotly_chart(px.histogram(df, x="frequency", nbins=30, title="Frequency Distribution"))
    st.plotly_chart(px.histogram(df, x="monetary", nbins=30, title="Monetary Distribution"))

with tab2:
    if "Segment_Name" in df.columns:
        st.subheader("🔍 Segment Breakdown")
        st.plotly_chart(px.pie(df, names="Segment_Name", title="Customer Segment Distribution"))

        st.markdown("#### 📋 Segment Sample Data")
        st.dataframe(df.head(100))
    else:
        st.warning("Segmentation data not available in raw RFM view.")

with tab3:
    st.subheader("🔎 Search by Customer ID")
    search_id = st.text_input("Enter CustomerID (e.g., C1010011):")

    if search_id:
        result = df[df["CustomerID"] == search_id]
        if not result.empty:
            st.success("Customer found.")
            st.write(result.T)
        else:
            st.error("Customer ID not found in current dataset view.")

# Footer
st.caption("Built with ❤️ using Streamlit | BankTrust RFM Dashboard")
