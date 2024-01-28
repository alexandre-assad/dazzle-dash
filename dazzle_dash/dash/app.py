
from dash import Dash, html, dcc
import plotly.express as px

import pandas as pd
from os import path


from ..dash.callbacks import all_calbacks

from importnb import Notebook

def app():

    df = Notebook.load_file(path.abspath("./notebooks/exploratory_analysis.ipynb")).df

    app = Dash(__name__)

    app.layout = html.Div([
        html.H1(children='Food We Eat', style={'textAlign':'center'}),
        
        dcc.Dropdown(df.Item.unique(), 'France', id='country-selection'),
        dcc.Graph(id='five_producers'),
        dcc.Dropdown(df.Item.unique(), 'Sugar cane', id='item-selection'),
        dcc.Graph(
            id='scat_geo')
    ])

    all_calbacks(df)
    

    if __name__ == "__app__":
        app.run(debug=True)