from dash import callback, Output, Input
import pandas as pd

import plotly.express as px
import matplotlib.pyplot as plt

from .functions import get_year_production

def all_calbacks(df: pd.DataFrame):
    @callback(
        Output('five_producers', 'figure'),
        Input('country-selection', 'value')
    )
    def five_best_producers(item):
        df.info()
        df_2013 = df.copy()
        df_2013['years_evolution'] = df["years_evolution"].apply(get_year_production, args=(52,))
        # Filtrer les données pour 'Sugar cane'
        df_item = df_2013[df_2013['Item'] == item]

        # Trier le DataFrame par la colonne 'Y2013' en ordre décroissant
        df_item_sorted = df_item.sort_values('years_evolution', ascending=False)

        # Sélectionner les 5 premières lignes
        df_item_top5 = df_item_sorted.head(5)
        # Créer un graphique à barres
        plt.figure(figsize=(10,6))
        plt.bar(df_item_top5['Area'], df_item_top5['years_evolution'], color='skyblue')
        plt.title(f'Top 5 des pays pour la production de {item} en 2013', fontsize=14)
        plt.xlabel('Pays', fontsize=12)
        plt.ylabel('Production', fontsize=12)
        plt.xticks(rotation=90)
        plt.grid(axis='y')
        plt.show()

    # @callback(
    #     Output('scat_geo', 'figure'),
    #     Input('item-selection', 'value')
    # )
    # def map_scatter(value):
    #     return px.scatter_geo(df.loc[df["Item"]==value], lat="latitude", lon = "longitude", size=year)