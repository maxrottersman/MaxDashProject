import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table as dash_table
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


fig6line = px.scatter(dfresult, x="Time", 
                       y="Wind Speed", 
                      color="Date",
                      title = "Wind Speed per hour",
                      hover_data=["Feed 1", "Feed 2"],
                     template=**dark**)



     app.layout = html.Div([
                  html.Div([dcc.Graph(id="g6",style={"width":graphwidth,
                                              "height": graphheight,
                                               'display': 'inline-block', 
                                               
                                               'horizontal-align': 'right',
                                               })




@app.callback(Output("g6", "style"),[Input("drop-temp", "value")])
    def update_style(value):
    return {"template":"value"}