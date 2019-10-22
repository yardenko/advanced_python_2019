import pandas as pd
import psutil

pd.set_option("display.max_colwidth" , 300)

df_high_level = pd.DataFrame(
    data=[
        {'day': 'Monday', 'Topic': 'Check-In, recaps and functions'},
        {'day': 'Tuesday', 'Topic': 'Coding philosophy, data flow and some more useful std modules'},
        {'day': 'Wednesday', 'Topic': 'Test driven development, python module, sphinx'},
        {'day': 'Thursday', 'Topic': 'OOP - Object oriented programming'},
        {'day': 'Friday', 'Topic': 'Q&A and code clean up'},
        {'day': '', 'Topic': ''},
        {'day': 'Monday', 'Topic': ''},
        {'day': 'Tuesday', 'Topic': ''},
        {'day': 'Wednesday', 'Topic': ''},
        {'day': 'Thursday', 'Topic': ''},
        {'day': 'Friday', 'Topic': 'Q&A and Tutorium'},


    ]
)

df_details = pd.DataFrame(
    data=[
        {'day': 1, 'Topic': 'Check-in'},
        {'day': 1, 'Topic': 'Procedural stuff'},
        {'day': 1, 'Topic': "python basic in 5'"},
        {'day': 1, 'Topic': 'lists and generators'},
        {'day': 1, 'Topic': 'bisect module'},
        # ----------------------------
        {'day': 2, 'Topic': 'Functions'},
        {'day': 2, 'Topic': 'Zen of Python and general coding philosophy'},
        {'day': 2, 'Topic': 'csv module'},
        {'day': 2, 'Topic': 'Collections module'},
        {'day': 2, 'Topic': 'Exercises 1 & 2'},
        # ----------------------------
        {'day': 3, 'Topic': 'Basic plotting with plotly'},
        {'day': 3, 'Topic': "String format"},
        {'day': 3, 'Topic': 'dicts'},
        {'day': 3, 'Topic': 'itertools'},
        {'day': 3, 'Topic': 'data flow'},
        {'day': 3, 'Topic': 'Exercises 3 & 4'},
        # -----------------------------
        {'day': 3, 'Topic': "Basic Python package"},
        {'day': 3, 'Topic': "Test Driven development"},
        {'day': 3, 'Topic': "Auto documentation with Sphinx"},
        # -----------------------------
        {'day': 4, 'Topic': "OOP"},
    ]
)


def display_topics(day=1, df=None):
    if df is None:
        df = df_details
    return df[df['day'] == day][['day', 'Topic']].head(20)
