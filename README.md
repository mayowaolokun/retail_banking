# 🏦 RFM-Based Customer Segmentation for Retail Banking

An interactive Streamlit dashboard and machine learning pipeline to segment retail banking customers using RFM (Recency, Frequency, Monetary) analysis and KMeans clustering. This tool empowers BankTrust to personalize services, reduce churn, and enhance marketing efficiency.

---

## 📌 Project Overview

In today’s competitive financial landscape, customer expectations are higher than ever. This project brings a data-driven solution to BankTrust's key challenges—**customer churn**, **inefficient marketing**, and **lack of personalization**—by leveraging customer transaction data.

Using **RFM analysis** and **unsupervised learning (KMeans clustering)**, the project categorizes customers into behavioral segments and presents them via a user-friendly **Streamlit dashboard**.

---

## 🎯 Business Objectives

- 🧠 Understand customer behavior using RFM metrics
- 🎯 Target marketing efforts toward high-value and at-risk segments
- 🤝 Improve customer retention through tailored engagement
- 📈 Enable non-technical teams to explore insights visually

---

## 🔬 Data Description

| Field              | Description                                           |
|-------------------|-------------------------------------------------------|
| `CustomerID`       | Unique customer identifier                           |
| `TransactionDate`  | Date of the transaction                              |
| `TransactionAmount`| Amount of transaction in local currency              |
| `recency_days`     | Days since last transaction                          |
| `frequency`        | Number of transactions by customer                   |
| `monetary`         | Total value of transactions                          |
| `Cluster`          | Cluster ID from KMeans                               |
| `Segment_Name`     | Descriptive segment label (e.g. Active High Value)   |

---

## 🧪 Project Pipeline

### 1. RFM Feature Engineering
- **Recency** – Days since the customer's most recent transaction
- **Frequency** – Number of transactions over the observed period
- **Monetary** – Total transaction value over the observed period

### 2. Unsupervised Clustering (KMeans)
- Trained on normalized RFM features
- Optimal number of clusters chosen via the elbow method
- Segments assigned human-readable names for business usability:
  - `Active High Value`
  - `Loyal Frequent Buyers`
  - `Big Spenders - At Risk`
  - `Low Value / One-time`

### 3. Streamlit Dashboard
- Visualizes RFM distributions
- Filters customers by RFM metrics and segment
- Displays per-customer profiles
- Supports toggling between raw and clustered datasets

---

## 🖥️ Streamlit Dashboard Features

| Feature                     | Description                                                  |
|----------------------------|--------------------------------------------------------------|
| 📊 RFM Overview            | Histograms for Recency, Frequency, and Monetary              |
| 🧠 Segmentation View       | Pie charts, tables, and filters by behavioral segments       |
| 🔍 Customer Lookup         | Search by `CustomerID` to view individual RFM + segment      |
| 🔧 Interactive Filtering   | Sidebar sliders to filter RFM values across dataset views    |

---

## 📁 Project Structure

project-root/
├── data/
│   ├── rfm_table.csv
│   └── KMeans_Customer_Segment_Table.csv
├── output/
│   └── app.py
├── notebooks/
│   ├── rfm_segmentation.ipynb
│   └── rfm_segmentation_unsupervised.ipynb
└── README.md

🚀 Getting Started
✅ Prerequisites

Install dependencies with pip (preferably inside a virtual environment):
pip install streamlit pandas plotly scikit-learn


▶️ Running the App
cd output
streamlit run app.py

⚠️ Ensure data/ is at the same level as output/.

| Segment Name           | Description                                   |
| ---------------------- | --------------------------------------------- |
| Active High Value      | Recent, frequent, and high-spending customers |
| Loyal Frequent Buyers  | Visit often but with average monetary value   |
| Big Spenders - At Risk | High spending, low recency                    |
| Low Value / One-time   | Infrequent customers with minimal engagement  |

## 📈 Business Impact
This solution enables BankTrust to:

📉 Reduce churn by identifying disengaged but valuable clients
🎯 Personalize offers by segment-specific strategies
💰 Optimize marketing by focusing resources on high-ROI segments
🧩 Democratize analytics through no-code interactive dashboards

## ⚙️ Tech Stack
Python – Core language
Pandas / NumPy – Data wrangling and feature engineering
Scikit-learn – KMeans clustering
Plotly – Interactive visualizations
Streamlit – Dashboarding and deployment

## 📦 Future Enhancements

📤 Upload new datasets via dashboard
📥 Export filtered segments to CSV
📊 2D/3D cluster visualizations using PCA or t-SNE
💬 What-if simulation tools for customer profiling
🔐 Authentication for segmented access control

## 📚 Acknowledgment
This project was developed as part of a Data Science specialization track in customer segmentation and unsupervised learning. It applies real-world business strategies to banking data analytics.