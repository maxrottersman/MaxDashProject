# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.graph_objs as go

from dash.dependencies import Input, Output



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph'    
    )
])

def prepare_chart_bar_data():
    # In real world, below prob done something like...
    # df2018= pd.read_sql('mySQL',db)
    data2018 = [['January', 6], ['February', 7], ['March', 2]] 
    data2019 = [['January', 7], ['February', 12], ['March', 5]] 
    df2018 = pd.DataFrame(data2018, columns = ['Month', 'SnowDays']) 
    df2019 = pd.DataFrame(data2019, columns = ['Month', 'SnowDays']) 

    # Assemble our list data for graphic, we'll use the plotly graph object "go"
    
    bars_data_set_a = {'data':
        [
        {'x': df2018['Month'].tolist(),
        'y': df2018['SnowDays'].tolist(),
        'type':'bar',
        'name':'2018'}
        ]
        }

    bars_data_set_b = {'data':
        [
        {'x': df2019['Month'].tolist(),
        'y': df2019['SnowDays'].tolist(),
        'type':'bar',
        'name':'2019'}
        ],
        'layout': {'title':'visualization'}}

    #my_figure_dict = dict(bars_data_set_a, **bars_data_set_b)
    bars_data_set_a.update(bars_data_set_b)

    my_figure_dict = bars_data_set_a

    return my_figure_dict


@app.callback(
    Output('example-graph', 'figure'),
    [Input('example-graph', '')])
def update_figure(figure):
    return prepare_chart_bar_data()

if __name__ == '__main__':
    app.run_server(debug=True)

    
    # data': [
    #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
    #             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    #         ],
    #         'layout': {
    #             'title': 'Dash Data Visualization'

    
    
    # return {
    #         'data': [
    #             {'x': df2018['Month'], 'y': df2018['SnowDays'], 'type': 'bar', 'name': '2018'},
    #             {'x': df2019['Month'], 'y': df2019['SnowDays'], 'type': 'bar', 'name':  '2019'},
    #         ],
    #         'layout': {
    #             'title': 'Dash Data Visualization'
    #         }
    #     }

    


 

