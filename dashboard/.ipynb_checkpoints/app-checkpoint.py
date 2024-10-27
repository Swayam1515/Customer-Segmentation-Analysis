import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv('../data/clustered_customer_data.csv')

# Title
st.title('Customer Segmentation Dashboard')

# Sidebar for cluster selection
selected_cluster = st.sidebar.selectbox('Select Cluster', data['Cluster'].unique())

# Filter data by selected cluster
cluster_data = data[data['Cluster'] == selected_cluster]

# Plot
fig = px.scatter(cluster_data, x='Annual_Income', y='Spending_Score', color='Cluster',
                 title=f'Cluster {selected_cluster} Customers',
                 labels={'Annual_Income': 'Annual Income', 'Spending_Score': 'Spending Score'})
st.plotly_chart(fig)

# Run Streamlit app
# streamlit run dashboard/app.py
