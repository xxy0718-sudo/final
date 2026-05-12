import streamlit as st
from movie_data import load_data
from sidebar import sidebar_filters
from charts import (
    genre_chart,
    release_trend_chart,
    rating_chart,
    style_chart,
    budget_rating_chart
)
from visual_style import visual_style_summary

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Movie Visual Trends Dashboard",
    layout="wide"
)

# --------------------------------------------------
# Load Data
# --------------------------------------------------
df = load_data()

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------
filtered_df = sidebar_filters(df)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("🎬 Movie Visual Trends Dashboard")

st.markdown(
    "Analyze movie genres, ratings, release trends, and cinematic visual styles through interactive data visualization."
)

# --------------------------------------------------
# Overview Metrics
# --------------------------------------------------
st.subheader("📊 Dashboard Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Movies", len(filtered_df))

with col2:
    st.metric("Average Rating", round(filtered_df['Rating'].mean(), 1))

with col3:
    st.metric("Average Budget", f"${round(filtered_df['Budget'].mean(), 1)}M")

# --------------------------------------------------
# Dataset Table
# --------------------------------------------------
st.subheader("🎞 Movie Dataset")
st.dataframe(filtered_df)

# --------------------------------------------------
# Charts
# --------------------------------------------------
genre_chart(filtered_df)
release_trend_chart(filtered_df)
rating_chart(filtered_df)
style_chart(filtered_df)
budget_rating_chart(filtered_df)

# --------------------------------------------------
# Visual Style Summary
# --------------------------------------------------
visual_style_summary()
