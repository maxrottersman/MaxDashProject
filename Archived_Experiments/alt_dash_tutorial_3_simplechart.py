import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table as dash_table
from dash.dependencies import Input, Output

import pandas as pd
from sqlalchemy import create_engine

from pathlib import Path

import plotly.graph_objects as go
import plotly.express as px

# Where is our database, wherever we're running this?
# and let's abstract with SQLAlchemy
ScriptPath = Path.cwd()
dbPath = ScriptPath / 'data'
dbPathandFileStr = str(dbPath / 'ETFdata.sqlite')
dbPathandFile = dbPath / 'ETFdata.sqlite'
db_uri = r'sqlite:///' + str(dbPathandFile)

# Connect to our db from SQLAlchemy
global db # make global so DASH can always get
global df # make global so DASH can always get
db = create_engine(db_uri)

df= pd.read_sql_table('Data_ETFs',db)
# Unique Managers for Drop Down
mgrs = sorted(df['Manager'].unique())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#
# PART 1, create our clean DASH layout object
#
app.layout = html.Div([
    dcc.Input(id='initialize_app_components_with_dummy_callback', value='', type='text', style={'display':'none'}),
    dcc.Dropdown(id='mgr-dropdown'), 
    html.Div(id='table-container'),
    dcc.Graph(id='graph-container')
])
#
# PART 2, set up the initial data in our DASH layout
#
@app.callback(
    Output(component_id='mgr-dropdown', component_property='options'),
    [Input(component_id='initialize_app_components_with_dummy_callback', component_property='value')]
)
def mgr_dropdown_BuildOptions(df_for_dropdown):  
    OptionList = [{'label': mgr, 'value': mgr} for mgr in mgrs]
    return OptionList
#
# PART 3, set up our callbacks to hands dropdown selections, etc
#

#
# Callback: Create table based on drop down selection
#
@app.callback(
    dash.dependencies.Output('table-container', 'children'),
    [dash.dependencies.Input('mgr-dropdown', 'value')])
def gen_table(dropdown_value):
    is_Manager = df['Manager']==dropdown_value
    # Create dataframe of those rows only by passing in those booleans
    dff = df[is_Manager] # dff as in dataframe filtered

    return html.Table(
    # Header
    [html.Tr([html.Th(col) for col in dff.columns])] +

    # Body
    [html.Tr([
        html.Td(dff.iloc[i][col]) for col in dff.columns
    ]) for i in range(min(len(dff), 5))])       

@app.callback(
    dash.dependencies.Output('graph-container', 'figure'),
    [dash.dependencies.Input('mgr-dropdown', 'value')])
def gen_graph(dropdown_value):
    is_Manager = df['Manager']==dropdown_value
    # Create dataframe of those rows only by passing in those booleans
    dff = df[is_Manager] # dff as in dataframe filtered
    fig = px.scatter(dff, x=dff['Expense Ratio'], y=dff.Assets)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)