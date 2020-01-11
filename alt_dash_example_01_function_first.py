# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

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

@app.callback(
    Output('example-graph', 'figure'),
    [Input('example-graph', '')])
def update_figure(figure):
    return {
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }

if __name__ == '__main__':
    app.run_server(debug=True)


# >From DASH tutorial, does this work?
# When the Dash app starts, it automatically calls all of the callbacks
# with the initial values of the input components in order to populate 
# the initial state of the output components

# OUTPUT in our data centric approach is our INPUT!
# In DASH's layout first approach, the INPUT is from the component in the layout
# and the OUTPUT is the changes dictated by that user change in input.   
 

