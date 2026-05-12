import streamlit as st


def sidebar_filters(df):
    st.sidebar.header("🎛 Filter Movies")

    selected_genre = st.sidebar.multiselect(
        "Select Genre",
        options=df["Genre"].unique(),
        default=df["Genre"].unique()
    )

    selected_country = st.sidebar.multiselect(
        "Select Country",
        options=df["Country"].unique(),
        default=df["Country"].unique()
    )

    selected_style = st.sidebar.multiselect(
        "Select Visual Style",
        options=df["Visual_Style"].unique(),
        default=df["Visual_Style"].unique()
    )

    filtered_df = df[
        (df["Genre"].isin(selected_genre)) &
        (df["Country"].isin(selected_country)) &
        (df["Visual_Style"].isin(selected_style))
    ]

    return filtered_df
