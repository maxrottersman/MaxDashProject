import dash 
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output,State
import datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import csv
#load external css stylesheet for basic design
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

###################################################
#load csv files and preprocessing data for plotting
###################################################
dfresult = pd.read_csv("1.csv", sep=",")
dfradar =  pd.read_csv("2.csv", sep=",")
dfoutput = pd.read_csv("3.csv", sep=",")
dfavg = pd.read_csv("4.csv",sep=",")

#set template, choose one of them
templates = ['ggplot2', 'seaborn', 'simple_white', 'plotly','plotly_white', 'plotly_dark', 'presentation', 'xgridoff', 'ygridoff', 'gridon']
dark = "seaborn"


def template_picker(template):
    dark = template
    return dark

###################################################
#creating figures (charts)
###################################################
#1 chart barchart, predicted day and similar
fig1bar = px.bar(dfbar1, x='Date',
                 y='Consumption',
                 hover_data=["Date", "Consumption"],
                 labels={'Consumption':'kW/h Consumption'},
                 color='Date',
                 text="Date",
                 title = "Demand ",
                 template = dark
                 
                 )
fig1bar.update_xaxes(type = 'category')
name = []
name = dfbar1.Date.unique().tolist()
for i in range(len(fig1bar.data)):
    fig1bar.data[i].update(name=str(name[i]))

#2 chart
    fig2line = px.scatter(dfresult, x="Time", 
                      y="Consumption", 
                      color="Date",
                      title = "Demand on Similar Days ",
                      template=dark)

name = []
name = dfresult.Date.unique().tolist()

fig2line.update_layout(hovermode='closest')
for i in range(len(fig2line.data)):
    fig2line.data[i].update(mode='markers+lines',name=str(name[i]))

app.layout = html.Div([                 
                    html.Button('Update Charts', id='button2',
                                style={
                                                    "width": "auto",
                                                    "float":"right",
                                                    'display': 'inline-block'
                                                   }),

                    dcc.Dropdown(id='drop-temp',
                                 style={
                                       
                                        "height": "2em",
                                        "display": 'inline-block',
                                        "width": "15em"
                                        
                                        },
                                    options=[{'label': str(i), 'value': i} for i in templates]
                                        ,placeholder="Select Template"
                                    )],
                  

                    html.Div(id="empty slot2",style={"height": "10px"}),

                    html.Div([id="graphplotter",

                        dcc.Interval(id='interval-component2',
                                    interval=1*1000, # in milliseconds
                                    n_intervals=0
                                    ),
                                
                        dcc.Graph(id="g1",style=
                            {"width":graphwidth,
                            "height": graphheight,
                            'display': 'inline-block', 
                            'horizontal-align': "left",                
                            },
                            figure=fig1bar,),
                        
                        dcc.Graph(id="g2",style=
                            {"width":graphwidth,
                            "height": graphheight,
                            'display': 'inline-block', 
                            'horizontal-align': 'middle',
                            }, 
                            figure=fig2line,)
                    ]
                    )
                             
if __name__ == "__main__":
    app.run_server()