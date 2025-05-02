import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title("Competitor Analysis Dashboard")

# Load the data (adjust the path based on where your file is located)
data = pd.read_csv("/Users/air/Documents/data-ingestion/google_play_apps.csv")

# Clean column names (remove extra spaces, if any)
data.columns = data.columns.str.strip()

# Check the available columns in the dataset
st.write("Columns in the dataset:", data.columns)

# Ensure that the necessary columns are present
if 'Title' in data.columns and 'Star_rating' in data.columns:
    # Sidebar filter for selecting applications
    st.sidebar.header("Filters")
    selected_apps = st.sidebar.multiselect(
        "Select applications", 
        options=data['Title'].unique(),
        default=data['Title'].unique()
    )

    # Filter data based on selected applications
    filtered_data = data[data['Title'].isin(selected_apps)]

    # Displaying key metrics in two columns
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Number of Apps", len(filtered_data))
    with col2:
        st.metric("Average Rating", f"{filtered_data['Star_rating'].mean():.2f}")

    # Create tabs for different visualizations
    tab1, tab2, tab3 = st.tabs(["Rating Comparison", "Rating Distribution", "Link to App"])

    # Tab 1: Bar Chart for Rating Comparison
    with tab1:
        fig = px.bar(filtered_data, x='Title', y='Star_rating', title="Rating Comparison")
        st.plotly_chart(fig)

    # Tab 2: Pie Chart for Rating Distribution
    with tab2:
        fig = px.pie(filtered_data, values='Star_rating', names='Title', title="Rating Distribution")
        st.plotly_chart(fig)

    # Tab 3: Display links to the applications
    with tab3:
        linkified_df = filtered_data[['Title', 'Star_rating', 'Link']].reset_index(drop=True)
        linkified_df['Link'] = linkified_df['Link'].apply(lambda x: f'<a href="{x}" target="_blank">Go to App</a>')
        st.write(linkified_df[['Title', 'Star_rating', 'Link']].to_html(escape=False), unsafe_allow_html=True)

    # Displaying filtered data in a table
    st.subheader("Filtered Applications Data")
    st.dataframe(filtered_data[['Title', 'Star_rating', 'Link']].reset_index(drop=True))
else:
    st.error("Required columns (Title and Star_rating) are not found in the dataset.")
