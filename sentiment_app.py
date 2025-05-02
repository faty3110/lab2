import streamlit as st
import pandas as pd
import plotly.express as px

# Title 
st.title("Sentiment Analysis of Google Play Apps")

# Load the data we scrapped in lab1
data = pd.read_csv("/Users/air/Documents/data-ingestion/google_play_apps.csv")

# Sentiment classification based on star rating
def classify_sentiment(star_rating):
    if star_rating >= 4:
        return "Positive"
    elif star_rating > 2:
        return "Neutral"
    else:
        return "Negative"

# Apply sentiment classification to the 'Star_rating' column
data["Sentiment"] = data["Star_rating"].apply(classify_sentiment)

# Sidebar for filtering options based on sentiment
st.sidebar.header("Filters")
selected_sentiment = st.sidebar.multiselect(
    "Filter by sentiment", 
    options=data["Sentiment"].unique(),
    default=data["Sentiment"].unique()
)

# Filter the data based on selected sentiment
filtered_data = data[data["Sentiment"].isin(selected_sentiment)]

# Displaying key metrics for filtered data
st.metric("Total Number of Apps", len(filtered_data))
st.metric("Average Star Rating", round(filtered_data["Star_rating"].mean(), 2))

# Bar Chart: Sentiment Distribution
st.subheader("Sentiment Distribution")
fig = px.histogram(filtered_data, x="Sentiment", color="Sentiment", barmode="group", title="Sentiment Distribution")
st.plotly_chart(fig)

# Displaying detailed filtered data in a table 
st.subheader("Filtered Application Data")
st.dataframe(filtered_data[["Title", "Star_rating", "Sentiment", "Link"]].reset_index(drop=True))
