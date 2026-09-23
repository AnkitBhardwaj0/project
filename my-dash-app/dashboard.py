import pandas as pd
import plotly.graph_objs as go
import numpy as np 
from dash import html
from dash import dcc
import dash

data=pd.read_csv(r'my-dash-app\gapminder.csv')

app=dash.Dash()
app.layout=html.Div([
     html.Div(children=[html.H1("My First Dashboard",style={'color':'red','text-align':'center'})],style={'border':'1px black solid','float':'left','width':'100%','height':'50px'}),
     html.Div(children=[
          dcc.Graph(id='Scatter-plot',figure={'data':[go.Scatter(x=data['time'],y=data['cell_phones_per_100_people'],mode='markers')],'layout':go.Layout(title='Scatter Plot')})
     ],style={'border':'1px black solid','float':'left','width':'49.7%'}),
     html.Div(children=[
          dcc.Graph(id='box-plot',figure={'data':[go.Box(x=data['agriculture_percent_of_gdp'])],'layout':go.Layout(title="Boxplot")})
     ],style={'border':'1px black solid','float':'left','width':'49.7%','height':'350px'})
])

if __name__ == "__main__":
     app.run()