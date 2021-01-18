import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import cdata.googleads as mod
import plotly.graph_objs as go
 
cnxn = mod.connect("DeveloperToken=MyDeveloperToken;ClientCustomerId=MyClientCustomerId;InitiateOAuth=GETANDREFRESH;OAuthSettingsLocation=/PATH/TO/OAuthSettings.txt")
 
df = pd.read_sql("SELECT Device, Clicks FROM CampaignPerformance WHERE Device = ''Mobile devices with full browsers''", cnxn)
app_name = 'dash-googleadsdataplot'
 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'CData + Dash'
trace = go.Bar(x=df.Device, y=df.Clicks, name='Device')
 
app.layout = html.Div(children=[html.H1("CData Extension + Dash", style={'textAlign': 'center'}),
dcc.Graph(
id='example-graph',
figure={
'data': [trace],
'layout':
go.Layout(title='Google Ads CampaignPerformance Data', barmode='stack')
})
], className="container")
 
if __name__ == '__main__':
    app.run_server(debug=True)