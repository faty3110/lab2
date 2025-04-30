import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Competitor Analysis Dashboard")

data = pd.DataFrame({
    'Company': ['Apple', 'Samsung', 'Google', 'Microsoft', 'Amazon'],
    'Market Share (%)': [25, 22, 15, 18, 20],
    'Revenue (Billion $)': [394, 245, 283, 198, 386],
    'Customer Satisfaction': [4.7, 4.5, 4.6, 4.3, 4.4]
})

st.sidebar.header("Filters")
selected_companies = st.sidebar.multiselect(
    "Select companies", 
    options=data['Company'].unique(),
    default=data['Company'].unique()
)

filtered_data = data[data['Company'].isin(selected_companies)]

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Companies", len(filtered_data))
with col2:
    st.metric("Average Market Share", f"{filtered_data['Market Share (%)'].mean():.1f}%")

tab1, tab2, tab3 = st.tabs(["Market Share", "Revenue", "Satisfaction"])

with tab1:
    fig = px.bar(filtered_data, x='Company', y='Market Share (%)', title="Market Share Comparison")
    st.plotly_chart(fig)

with tab2:
    fig = px.pie(filtered_data, values='Revenue (Billion $)', names='Company', title="Revenue Distribution")
    st.plotly_chart(fig)

with tab3:
    fig = px.scatter(filtered_data, x='Market Share (%)', y='Customer Satisfaction', 
                    size='Revenue (Billion $)', color='Company', 
                    title="Market Share vs Customer Satisfaction")
    st.plotly_chart(fig)