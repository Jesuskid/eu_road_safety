
## Installation

**Installation Requirements**
- Python >= 3.9
- bs4(BeautifulSoup) >= 0.0.1
-pandas >= 1.3.1
*For visualization only*
- dash >= 1.21.0
- plotly >= 5.1.0



## Getting Started

Here's a quick run of how to use this script to get the data on 
[Road_safety_in_Europe](https://en.wikipedia.org/wiki/Road_safety_in_Europe). From Wikidpedia
# Run this app with `python main.py` and

1. Import the libraries
  ```python
  from bs4 import BeautifulSoup
  import pandas as pd
  import requests

  ```

2. Get the Data from Wikipedia using Html requests and bs4(BeautifulSoup)
	```python
response = requests.get('https://en.wikipedia.org/wiki/Road_safety_in_Europe')
url = response.text
soup = BeautifulSoup(url, 'html.parser')

table = soup.find(class_='wikitable sortable')

```

3. Convert the data into a dataFrame
	```python
	df = pd.read_html(table.prettify())			
	```
4.Transform and clean the data 
  Eliminate columns not used and change column names and create a new dataframe

	```python
  	new_df = df[0].rename(columns={
    'Country': 'Country',
    'Area  (thousands of km  2  )  [24]': 'Area',
    'Population in 2018  [25]': 'Population',
    'GDP per capita in 2018  [26]': 'GDP per capita',
    'Population density  (inhabitants per km  2  ) in 2017  [27]': 'Population density',
    'Vehicle ownership  (per thousand inhabitants) in 2016  [28]': 'Vehicle ownership',
    'Total Road Deaths in 2018  [30]': 'Total road deaths',
    'Road deaths  per Million Inhabitants in 2018  [30]': 'Road deaths per Million Inhabitants',

})

new_df.drop(['Road Network Length  (in km) in 2013  [29]',
             'Number of People Killed  per Billion km  [30]',
             'Number of Seriously Injured in 2017/2018  [30]'],
            axis=1, inplace=True)
			
	```
5. Create and insert the year column
```python
year_column = [2018 for i in range(29)]
new_df.insert(1, 'Year', year_column)
```

6. Sort the data
```python
sorted_df = new_df.sort_values(by='Road deaths per Million Inhabitants')


```

7. Convert the new dataframe to a csv file
```python
# Converts the dataframe to csv
sorted_df.to_csv("myfile.csv", index=False)
```

##Lets Visualize the data with dash(use the viuslize script)

# Run this app with `python visualize.py` and
# visit http://127.0.0.1:8050/ in your web browser.

1. Import the libraries
```python
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
```

2. Initialize the dash app
```python
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
```

3. Get the data frame and plot it
```python
df = pd.read_csv('myfile.csv')
df.drop(eu_index, inplace = True)

fig = px.pie(df2, values='Road deaths per Million Inhabitants', names='Country', title='Road deaths per Million Inhabitants')


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
app.layout = html.Div(
    children=[
        html.H1(children='European Union Road Safety Visualizations'),
        html.Div(children='For the Challenge'),
        doc.Graph(
            id='chart',
            figure=fig
        )
    ]
)
```

4. Run the app
```python
if __name__ == '__main__':
    app.run_server(debug=True)
```

Now you have the proportion of road mortatility for each european country in the data set.