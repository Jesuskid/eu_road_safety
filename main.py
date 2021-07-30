from bs4 import BeautifulSoup
import pandas as pd
import requests

# Grabs the data from Wikipedia
response = requests.get('https://en.wikipedia.org/wiki/Road_safety_in_Europe')
url = response.text
soup = BeautifulSoup(url, 'html.parser')

table = soup.find(class_='wikitable sortable')

# Converts the raw data into a data-frame with pandas
df = pd.read_html(table.prettify())

# Data transformation goes on here, with the edit of new columns etc
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

year_column = [2018 for i in range(29)]
new_df.insert(1, 'Year', year_column)
sorted_df = new_df.sort_values(by='Road deaths per Million Inhabitants')
# Converts the dataframe to csv
sorted_df.to_csv("European_Union_Road_Safety.csv", index=False)
