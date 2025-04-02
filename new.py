from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
df = pd.read_csv(r'C:\Users\75047\Downloads\datasets(Sheet2) (2).csv', encoding='ISO-8859-1')
app = Dash()
server = app.server
app.layout = html.Div([
    html.H1(children='FIFA Winners', style={'textAlign':'center'}),
    html.H2("Select a Country:"),
    dcc.RadioItems(
        id='Countrys',
        options=[{'label':countrys, 'value':countrys} for countrys in df['Countrys'].unique()],
        value='Ireland',
        inline=True,
    ),
 
    dcc.Graph(id='graph-content'),
#])
    html.Div(id='year-output', style={'textAlign':'center','marginTop':'20px'}),
])
@callback(
    Output('graph-content', 'figure'),
    Input('Countrys', 'value')
)
def update_graph(value):
  

    dff = df[df.Countrys==value]
    

    #return px.choropleth(dff, y='Wins')
    fig = px.choropleth(
        dff,
        locations='Countrys',
        #featureidkey='properties.Countrys',
        color='Wins',
        color_continuous_scale="Viridis", 
        title=f'FIFA Winners',
        labels={'Wins':'Number of Wins'},  
        locationmode='country names',
        hover_name='Countrys'

    )
    fig.update_geos(showcoastlines=True, coastlinecolor="Black",projection_type="natural earth")
    return fig

        
if __name__ == '__main__':
    app.run(debug=True)