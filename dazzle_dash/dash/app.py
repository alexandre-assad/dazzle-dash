
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
        
        dcc.Dropdown(df.Item.unique(), 'Honey', id='item-selection'),
        dcc.Graph(
            id='all_time_producers'
        ),
        dcc.Graph(
            id='five_producers'
        )
    ])

    all_calbacks(df)
    app.run(debug=True)

