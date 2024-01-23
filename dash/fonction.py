
import plotly.express as px

import pandas as pd
from os import path

def food_country_line(value):
    dff = df[df.Area==value]
    return px.line(dff, x='Item', y='Y2013')


def map_scatter(value):
    return px.scatter_geo(df.loc[df["Item"]==value], lat="latitude", lon = "longitude", size="Y2013")