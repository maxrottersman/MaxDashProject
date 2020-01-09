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

# print(df.head())
# print(df.columns)
# print(df.shape)

#df_filtered = df.Manager.str.contains('PIMCO')

# Shows only Manager Column
#print(df.filter(["Manager"]))

# get boolean list of rows that match filter
is_Manager = df['Manager']=='PIMCO'
# create dataframe of those rows only by passing in those booleans
dff = df[is_Manager]
# view
print(dff.head())

# Creates HTML
#html = df.to_html()
#print(html)