import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table as dash_table
from dash.dependencies import Input, Output

import pandas as pd
from sqlalchemy import create_engine

from pathlib import Path

# Where is our database, wherever we're running this?
# and let's abstract with SQLAlchemy
ScriptPath = Path.cwd()
dbPath = ScriptPath / 'data'
dbPathandFileStr = str(dbPath / 'ETFdata.sqlite')
dbPathandFile = dbPath / 'ETFdata.sqlite'
db_uri = r'sqlite:///' + str(dbPathandFile)

# Connect to our db from SQLAlchemy
global db # make global so DASH can always get
global df
db = create_engine(db_uri)

df= pd.read_sql_table('Data_ETFs',db)
# Unique Managers for Drop Down
mgrs = sorted(df['Manager'].unique())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# options=[
#             {'label': mgr, 'value': mgr} for mgr in mgrs
#         ],
#         value=''

#
# PART 1, create our DASH layout object
#
app.layout = html.Div([
    dcc.Input(id='initialize_components_dummy_callback', value='', type='text', style={'display':'none'}),
    dcc.Dropdown(id='mgr-dropdown'), 
    html.Div(id='table-container')
])
#
# PART 2, set up the initial data in our DASH layout
#
@app.callback(
    Output(component_id='mgr-dropdown', component_property='options'),
    [Input(component_id='initialize_components_dummy_callback', component_property='value')]
)
def mgr_dropdown_BuildOptions(df_for_dropdown):  
    OptionList = [{'label': mgr, 'value': mgr} for mgr in mgrs]
    return OptionList



# Attach callback to div: initialize_components_dummy_callback

if __name__ == '__main__':
    app.run_server(debug=True)