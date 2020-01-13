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

    graph_bars_data = {'data':
        [
        {'x': df2018['Month'].tolist(),
        'y': df2018['SnowDays'].tolist(),
        'type':'bar',
        'name':'2018'},
        {'x': df2019['Month'].tolist(),
        'y': df2019['SnowDays'].tolist(),
        'type':'bar',
        'name':'2019'}
        ]
        }

    graph_layout = {'layout': {'title':'visualization'}}

    my_figure_dict = dict(graph_bars_data, **graph_layout) 
    
    return my_figure_dict

@app.callback(
    Output('example-graph', 'figure'),
    [Input('example-graph', '')])
def update_figure(figure):
    return prepare_chart_bar_data()

if __name__ == '__main__':
    app.run_server(debug=True)

    
        # return {
        #     'data': [
        #         {'x': df2018['Month'], 'y': df2018['SnowDays'], 'type': 'bar', 'name': '2018'},
        #         {'x': df2019['Month'], 'y': df2019['SnowDays'], 'type': 'bar', 'name':  '2019'},
        #     ],
        #     'layout': {
        #         'title': 'Dash Data Visualization'
        #     }
        # }

    
    
    # return {
    #         'data': [
    #             {'x': df2018['Month'], 'y': df2018['SnowDays'], 'type': 'bar', 'name': '2018'},
    #             {'x': df2019['Month'], 'y': df2019['SnowDays'], 'type': 'bar', 'name':  '2019'},
    #         ],
    #         'layout': {
    #             'title': 'Dash Data Visualization'
    #         }
    #     }

    


 

