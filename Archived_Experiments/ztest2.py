import pandas as pd
import plotly.graph_objects as go
from pandas import DataFrame
from sqlalchemy import create_engine

from pathlib import Path
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

is_Manager = df['Manager']=='PIMCO'
# Create dataframe of those rows only by passing in those booleans

dff = df[is_Manager] # dff as in dataframe filtered
dff_xy = DataFrame(dff,columns=['[Expense Ratio]','[Assets]'])

print(dff_xy.head())

#gapminder = px.data.gapminder()
#gapminder2007 = gapminder.query("year == 2007")

#mygraph = px.scatter(dff_xy, x="[Expense Ratio]", y="[Assets]")
#mygraph.show()



#data= pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")

# fig = go.Figure(dff_xy=go.Scatter(x=dff_xy['Expense Ratio'],
#                                 y=dff_xy['Assets'])) # hover text goes here

# fig.update_layout(title='Population of USA States')
# fig.show()

# https://plot.ly/python/plotly-express/
#df = px.data.iris()
fig = px.scatter(dff_xy, x=dff['Expense Ratio'], y=dff.Assets)
fig.show()