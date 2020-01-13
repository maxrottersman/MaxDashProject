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
# playing safe, making these global
global db, df, mgrs 
db = create_engine(db_uri)

# App's raw data
df= pd.read_sql('Select [Symbol],[Expense Ratio],[Assets],[Manager],[Category] From Data_ETFs',db)
# From that, create unique Managers for Drop Down
mgrs = sorted(df['Manager'].unique())

# Create our DASH app object!
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

#
# Part 1: DATA FUNCTIONS
#
#
#  Manager names for our dropdown, which drives table and chart
def data_mgr_options_build():
    OptionList = [{'label': mgr, 'value': mgr} for mgr in mgrs]
    return OptionList
#
#  Fill DATATABLE from Manager Dropdown List
def data_table_populat(dropdown_value):
    is_Manager = df['Manager']==dropdown_value
    # Create dataframe of those rows only by passing in those booleans
    dff = df[is_Manager] # dff as in dataframe filtered
    # Data table won't work without column defs
    my_table_columns = [{"name": i, "id": i,} for i in (df.columns)]
    
    return dff.to_dict('records'), my_table_columns
    
#
# Draw GRAPH from data picked in manager dropdown list
def data_graph_draw(dropdown_value):
    is_Manager = df['Manager']==dropdown_value
    # Create dataframe of those rows only by passing in those booleans
    dff = df[is_Manager] # dff as in dataframe filtered
    # Using HELPER library plotly.express as px
    fig = px.scatter(dff, x=dff['Expense Ratio'], y=dff.Assets)
    return fig

##### END DATA FUNCTIONS #####
#
# STYLES
#
# Give style same names as DASH uses, purpose here to keep app.layout ucluttered
#
style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Symbol', 'Manager', 'Category']
    ]
style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        }
    ]
style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    }

#
# PART 2, Create our clean DASH LAYOUT object
#
app.layout = html.Div([
    dcc.Input(id='initialize_app_components_with_dummy_callback', value='', type='text', style={'display':'none'}),
    dcc.Dropdown(id='mgr-dropdown'), 
    dash_table.DataTable(id='table-container',
        style_cell_conditional = style_cell_conditional,
        style_data_conditional = style_data_conditional,
        style_header = style_header),
    dcc.Graph(id='graph-container')
])
#
# PART 2, Load Initial DROPDOWN LIST DATA in our DASH layout which
# will happen after the app is run.
#
@app.callback(
    Output(component_id='mgr-dropdown', component_property='options'),
    [Input(component_id='initialize_app_components_with_dummy_callback', component_property='value')]
)
def mgr_dropdown_BuildOptions(df_for_dropdown):  
    return data_mgr_options_build()
#
# PART 3, set up our callbacks to hands dropdown selections, etc
#

#
# Callback: TABLE POPULATE based on drop down selection
#
@app.callback([Output('table-container', 'data'), Output('table-container', 'columns')],
    [Input('mgr-dropdown', 'value')])
def gen_table(dropdown_value):
    return data_table_populat(dropdown_value)
    
#
# Callback: GRAPH DRAW based on drop down selection
#  
@app.callback(
    dash.dependencies.Output('graph-container', 'figure'),
    [dash.dependencies.Input('mgr-dropdown', 'value')])
def gen_graph(dropdown_value):
    return data_graph_draw(dropdown_value)

###
### OKAY, LET 'ER RIP
###    

if __name__ == '__main__':
    # Can this ever work instead of dummy callback?
    #app.callback(Output('mgr-dropdown', 'options')) (mgr_options_build())
    
    app.run_server(debug=True)
