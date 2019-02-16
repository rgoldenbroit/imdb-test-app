import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

import plotly.plotly as py
from plotly.graph_objs import *

########### Set up the chart

#Reads in static data file.

source = '/Users/rgoldenbroit/Documents/GeneralAssembly/Final/imdb-test-app//imdb_1000.csv'
df = pd.read_csv(source)


#Define bar chat variables and display bar chart.

newvar = df.groupby('content_rating')['duration'].mean().sort_values().tolist()
newvar2 = df.groupby('content_rating')['duration'].mean().sort_values().keys().tolist()

fig = go.Bar(x=newvar2, y=newvar,
        name="Move duration vs content rating",
        marker = {'color:lightblue'},
        text=newvar
            )

graph_layout = go.Layout(
    title = 'Are more mature movies generally longer?'')

newfigure = go.Figure(layout=graph_layout)


# beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Summer Ale']
#
# bitterness = go.Bar(
#     x=beers,
#     y=[35, 60, 85, 20],
#     name='IBU',
#     marker={'color':'lightblue'}
# )
# alcohol = go.Bar(
#     x=beers,
#     y=[5.4, 7.1, 9.2, 3],
#     name='ABV',
#     marker={'color':'pink'}
# )
#
# beer_data = [bitterness, alcohol]
# beer_layout = go.Layout(
#     barmode='group',
#     title = 'Beer Comparison'
# )
#
# beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('IMDB-based Cool First App'),
    dcc.Graph(
        id='imdb1',
        figure=newfigure
    )]
)

if __name__ == '__main__':
    app.run_server()
