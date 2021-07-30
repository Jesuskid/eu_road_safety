from dash import Dash
import plotly.express as px
import dash_core_components as doc
import dash_html_components as html
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('European_Union_Road_Safety.csv')
df2 = pd.read_csv('European_Union_Road_Safety.csv')

eu_index = df2[ df2['Country'] == 'EU 28 Total' ].index
df2.drop(eu_index, inplace = True)
colors = {
    'background': '#fffff5',
    'text': '#7FDBFF'
}


fig = px.bar(df2, x='Country', y='Vehicle ownership', title='EU Vehicle Ownership Per 1000', barmode='group')
fig.update_layout(
)

fig2 = px.bar(df2, x="Country", y=["Population density", "Vehicle ownership", "Total road deaths"],
              title="Ratio of Population density, Vehicle ownership and Total road deaths per country")

fig3 = px.pie(df2, values='Road deaths per Million Inhabitants', names='Country', title='Road deaths per Million Inhabitants')

app.layout = html.Div(
    children=[
        html.H1(children='European Union Road Safety Visualizations'),
        html.Div(children='For the Challenge'),
        doc.Graph(
            id='chart',
            figure=fig
        ),
        doc.Graph(
            id='chart2',
            figure=fig2
        ),
       doc.Graph(
            id='chart3',
            figure=fig3
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)