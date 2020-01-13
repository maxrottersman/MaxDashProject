# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

from dash.dependencies import Input, Output



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Let's predent were' getting a dataframe from a database, but for now
# we'll create manually

# initialize list of lists 
data2018 = [['January', 10], ['February', 7], ['March', 2]] 
data2019 = [['January', 7], ['February', 12], ['March', 5]] 
# Create the pandas DataFrame 
df2018 = pd.DataFrame(data2018, columns = ['Month', 'SnowDays']) 
df2019 = pd.DataFrame(data2019, columns = ['Month', 'SnowDays']) 

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
                {'x': df2018['Month'], 'y': df2018['SnowDays'], 'type': 'bar', 'name': '2018'},
                {'x': df2019['Month'], 'y': df2019['SnowDays'], 'type': 'bar', 'name':  '2019'},
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
 

