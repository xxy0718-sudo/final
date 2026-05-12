import pandas as pd


def load_data():
    data = {
        "Movie": [
            "La La Land", "The Batman", "Parasite", "Interstellar",
            "Joker", "Avengers", "Your Name", "Inception",
            "Titanic", "Get Out"
        ],

        "Genre": [
            "Romance", "Action", "Drama", "Sci-Fi",
            "Drama", "Action", "Animation", "Sci-Fi",
            "Romance", "Horror"
        ],

        "Country": [
            "USA", "USA", "Korea", "USA",
            "USA", "USA", "Japan", "USA",
            "USA", "USA"
        ],

        "Release_Year": [
            2016, 2022, 2019, 2014,
            2019, 2018, 2016, 2010,
            1997, 2017
        ],

        "Rating": [
            8.0, 7.8, 8.5, 8.6,
            8.4, 8.0, 8.4, 8.8,
            7.9, 7.7
        ],

        "Visual_Style": [
            "Warm", "Dark", "Dark", "Cool",
            "Dark", "Cool", "Warm", "Cool",
            "Warm", "Dark"
        ],

        "Budget": [
            30, 185, 11, 165,
            70, 356, 5, 160,
            200, 4
        ]
    }

    return pd.DataFrame(data)
