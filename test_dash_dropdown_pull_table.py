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

db = create_engine(db_uri)

# DROP DOWN DATA
sql = "Select Manager from Data_ETFs_UniqueManagers where Manager <>''"
df_dropdown = pd.read_sql(sql = sql,con=db)
#conn = sqlite3.connect(dbPathandFileStr)
#cursor = conn.cursor()
#sql = "Select Manager from Data_ETFs_UniqueManagers where Manager <>''"
#cursor.execute(sql)
#lstManagers = [x[0] for x in list(cursor.fetchall())]
#conn.close()



# DASH table will ONLY work with SQLALCHEMY
db = create_engine(db_uri)
df = pd.read_sql_table('Data_ETFs',db)
mgrs = df['Manager']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(
        id='mgr-dropdown',
        options=[
            {'label': mgr, 'value': mgr} for mgr in mgrs
        ],
        value=''
    ),
    html.Div(id='dd-output-container'),

    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    )
])

@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('mgr-dropdown', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

# read later
# https://towardsdatascience.com/build-your-own-data-dashboard-93e4848a0dcf

# https://community.plot.ly/t/dash-datatable-updating-rows-with-dropdowns/6714

if __name__ == '__main__':
    app.run_server(debug=True)