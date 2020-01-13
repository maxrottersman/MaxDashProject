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
global df
df= pd.read_sql_table('Data_ETFs',db)
mgrs = sorted(df['Manager'].unique())

#
# We need to generate table outside layout so we can ALSO
# change the table through callbacks.
# so removed this and replaced with html.Div(id='table-container'):
#  html.Div(id='dd-output-container'),

#     dash_table.DataTable(
#     id='table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict('records'),
#     )
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

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
    html.Div(id='table-container')
   
])

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
    ]) for i in range(min(len(dff), 20))]
    )

# Userful for filtering dataframes
# https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/

# read later
# https://towardsdatascience.com/build-your-own-data-dashboard-93e4848a0dcf

# https://community.plot.ly/t/dash-datatable-updating-rows-with-dropdowns/6714

if __name__ == '__main__':
    app.run_server(debug=True)