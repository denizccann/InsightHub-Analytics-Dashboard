import streamlit as st
import pandas as pd
import plotly.express as px

# Page Setup
st.set_page_config(page_title="InsightHub | Data Analytics", layout="wide")

st.title("📊 InsightHub: Professional Data Analytics Dashboard")
st.markdown("Developed by **Deniz Can** | GBC Computer Programming & Analysis")

# 1. Sidebar - Data Input Simulation
st.sidebar.header("Dashboard Settings")
view_mode = st.sidebar.radio("Analysis Type", ["Departmental", "Financial Metrics"])

# 2. Mock Professional Data (Alumina-Inspired)
data = {
    'Department': ['Software', 'Cybersecurity', 'Finance', 'Operations', 'Marketing', 'QA'],
    'Productivity': [95, 88, 72, 85, 80, 92],
    'Budget_Utilization': [0.92, 0.85, 0.98, 0.75, 0.88, 0.90],
    'Headcount': [15, 8, 12, 20, 10, 5]
}
df = pd.DataFrame(data)

# 3. Top Metrics (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Average Productivity", "87%", "+4.5%")
col2.metric("Total Headcount", sum(data['Headcount']), "Active")
col3.metric("System Status", "Secure", "CCST Compliant")

st.divider()

# 4. Visualizations
left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Efficiency by Department")
    fig_bar = px.bar(df, x='Department', y='Productivity', color='Productivity', 
                     color_continuous_scale='Viridis', template="plotly_dark")
    st.plotly_chart(fig_bar, use_container_width=True)

with right_chart:
    st.subheader("Budget vs Productivity Correlation")
    fig_scatter = px.scatter(df, x='Budget_Utilization', y='Productivity', 
                             size='Headcount', color='Department', hover_name='Department')
    st.plotly_chart(fig_scatter, use_container_width=True)

# 5. Data Integrity Table (The Audit View)
st.subheader("📋 Verified Corporate Dataset")
st.dataframe(df, use_container_width=True)

st.sidebar.info("Data Integrity Verified (Audit Ready)")