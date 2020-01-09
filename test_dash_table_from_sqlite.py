import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table as dash_table

from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path

ScriptPath = Path.cwd()
dbPath = ScriptPath / 'data'
dbPathandFileStr = str(dbPath / 'ETFdata.sqlite')
dbPathandFile = dbPath / 'ETFdata.sqlite'
db_uri = r'sqlite:///' + str(dbPathandFile)

# DASH table will ONLY work with SQLALCHEMY
db = create_engine(db_uri)
df = pd.read_sql_table('Data_ETFs',db)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

# read later
# https://towardsdatascience.com/build-your-own-data-dashboard-93e4848a0dcf

if __name__ == '__main__':
    app.run_server(debug=True)