from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

import pandas as pd
from os import path

def main_app():
    df = pd.read_csv(path.join('.','data/raw','FAO.csv'), encoding='latin-1')

    app = Dash(__name__)

    app.layout = html.Div([
        html.H1(children='Food We Eat', style={'textAlign':'center'}),
        
        dcc.Dropdown(df.Area.unique(), 'France', id='country-selection'),
        dcc.Graph(id='food_per_country'),
        dcc.Dropdown(df.Item.unique(), 'Sugar cane', id='item-selection'),
        dcc.Graph(
            id='scat_geo')
    ])

    @callback(
        Output('food_per_country', 'figure'),
        Input('country-selection', 'value')
    )
    def food_country_line(value):
        dff = df[df.Area==value]
        return px.line(dff, x='Item', y='Y2013')

    @callback(
        Output('scat_geo', 'figure'),
        Input('item-selection', 'value')
    )
    def map_scatter(value):
        return px.scatter_geo(df.loc[df["Item"]==value], lat="latitude", lon = "longitude", size="Y2013")
    
    app.run(debug=True)


