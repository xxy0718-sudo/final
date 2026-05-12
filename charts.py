import streamlit as st
import plotly.express as px


# Genre Distribution
# --------------------------------------------------
def genre_chart(df):
    st.subheader("🎭 Genre Distribution")

    fig = px.pie(
        df,
        names="Genre",
        title="Movie Genre Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


# Release Year Trends
# --------------------------------------------------
def release_trend_chart(df):
    st.subheader("📅 Release Year Trends")

    year_count = df.groupby("Release_Year").size().reset_index(name="Count")

    fig = px.line(
        year_count,
        x="Release_Year",
        y="Count",
        markers=True,
        title="Movies Released by Year"
    )
  
    st.plotly_chart(fig, use_container_width=True)


# Ratings
# --------------------------------------------------
def rating_chart(df):
    st.subheader("⭐ Movie Ratings")

    fig = px.bar(
        df,
        x="Movie",
        y="Rating",
        color="Genre",
        title="Movie Rating Comparison"
    )

    st.plotly_chart(fig, use_container_width=True)


# Visual Style
# --------------------------------------------------
def style_chart(df):
    st.subheader("🎨 Visual Style Analysis")

    style_count = df.groupby("Visual_Style").size().reset_index(name="Count")

    fig = px.bar(
        style_count,
        x="Visual_Style",
        y="Count",
        color="Visual_Style",
        title="Visual Style Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


# Budget vs Rating
# --------------------------------------------------
def budget_rating_chart(df):
    st.subheader("💰 Budget vs Rating")

    fig = px.scatter(
        df,
        x="Budget",
        y="Rating",
        color="Visual_Style",
        size="Budget",
        hover_name="Movie",
        title="Budget and Audience Rating"
    )

    st.plotly_chart(fig, use_container_width=True)
