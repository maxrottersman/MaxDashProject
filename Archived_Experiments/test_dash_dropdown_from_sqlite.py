import dash
import dash_html_components as html
import dash_core_components as dcc

import sqlite3
import pandas as pd
from pathlib import Path

ScriptPath = Path.cwd()
dbPath = ScriptPath / 'data'
dbPathandFileStr = str(dbPath / 'ETFdata.sqlite')

conn = sqlite3.connect(dbPathandFileStr)
cursor = conn.cursor()
sql = "Select Manager from Data_ETFs_UniqueManagers where Manager <>''"
cursor.execute(sql)
#lstManagersT = list(cursor.fetchall())
lstManagers = [x[0] for x in list(cursor.fetchall())]
conn.close()
#lstManagers = ["test1", "test2"]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='mgr-dropdown',
        options=[
            {'label': mgr, 'value': mgr} for mgr in lstManagers
        ],
        value=''
    ),
    html.Div(id='dd-output-container')
])

# dcc.Dropdown(
#         id='demo-dropdown',
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': 'Montreal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value='NYC'
#     ),


# @app.callback(
#     dash.dependencies.Output('dd-output-container', 'children'),
#     [dash.dependencies.Input('demo-dropdown', 'value')])
# def update_output(value):
#     return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)