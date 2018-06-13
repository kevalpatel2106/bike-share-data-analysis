import pandas as pd


def load_chicago_data():
    return pd.read_csv("../chicago.csv")


def load_nyc_data():
    return pd.read_csv("../new_york_city.csv")


def load_washington_data():
    return pd.read_csv("../washington.csv")
