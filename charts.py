import streamlit as st
import plotly.express as px


# --------------------------------------------------
# Genre Distribution
# --------------------------------------------------
def genre_chart(df):
    st.subheader("🎭 Genre Distribution")

    fig = px.pie(
        df,
        names="Genre",
        hole=0.4,
        title="Movie Genre Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


# --------------------------------------------------
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


# --------------------------------------------------
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


# --------------------------------------------------
# Country Distribution
# --------------------------------------------------
def country_chart(df):
    st.subheader("🌍 Country Distribution")

    country_count = df.groupby("Country").size().reset_index(name="Count")

    fig = px.bar(
        country_count,
        x="Country",
        y="Count",
        color="Country",
        title="Movies by Country"
    )
    
    st.plotly_chart(fig, use_container_width=True)


# --------------------------------------------------
# Budget vs Rating
# --------------------------------------------------
def budget_rating_chart(df):
    st.subheader("💰 Budget vs Rating")

    fig = px.scatter(
        df,
        x="Budget",
        y="Rating",
        color="Genre",
        size="Budget",
        hover_name="Movie",
        title="Budget and Audience Rating"
    )

    st.plotly_chart(fig, use_container_width=
    

# --------------------------------------------------
# Top Movies
# --------------------------------------------------
def top_movies_chart(df):
    st.subheader("🏆 Top Rated Movies")

    top_df = df.sort_values(by="Rating", ascending=False)

    fig = px.bar(
        top_df,
        x="Movie",
        y="Rating",
        color="Rating",
        title="Top Rated Movies"
    )

    st.plotly_chart(fig, use_container_width=True)
