import streamlit as st
from movie_data import load_data
from sidebar import sidebar_filters
from charts import (
    genre_chart,
    release_trend_chart,
    rating_chart,
    country_chart,
    budget_rating_chart,
    top_movies_chart
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Movie Genre & Audience Trends Dashboard",
    page_icon="🎬",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }

    h1 {
        color: #FF4B4B;
        text-align: center;
    }

    h2, h3 {
        color: #F9F9F9;
         }

    .stMetric {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #333333;
    }

    .custom-card {
        background-color: #1A1D24;
        padding: 20px;
        border-radius: 20px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Load Data
# --------------------------------------------------
df = load_data()
filtered_df = sidebar_filters(df)

# --------------------------------------------------
# Header Section
# --------------------------------------------------
st.title("🎬 Movie Genre & Audience Trends Dashboard")

st.markdown(
    """
    <div class='custom-card'>
    Explore movie genres, ratings, audience preferences, and global film trends through interactive data visualization.
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Overview Metrics
# --------------------------------------------------
st.subheader("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🎞 Total Movies", len(filtered_df))

with col2:
    st.metric("⭐ Average Rating", round(filtered_df['Rating'].mean(), 1))

with col3:
    st.metric("🌍 Countries", filtered_df['Country'].nunique())

with col4:
    st.metric("💰 Average Budget", f"${round(filtered_df['Budget'].mean(), 1)}M")

# --------------------------------------------------
# Dataset Table
# --------------------------------------------------
st.subheader("🎥 Movie Dataset")
st.dataframe(filtered_df, use_container_width=True)

# --------------------------------------------------
# Charts Layout
# --------------------------------------------------
colA, colB = st.columns(2)

with colA:
    genre_chart(filtered_df)

with colB:
    release_trend_chart(filtered_df)

colC, colD = st.columns(2)

with colC:
    rating_chart(filtered_df)

with colD:
    country_chart(filtered_df)

# --------------------------------------------------
# Full Width Charts
# --------------------------------------------------
budget_rating_chart(filtered_df)

top_movies_chart(filtered_df)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")

st.markdown(
    """
    <center>
    🎬 Movie Genre & Audience Trends Dashboard <br>
    Created with Streamlit & Plotly
    </center>
    """,
    unsafe_allow_html=True
)
