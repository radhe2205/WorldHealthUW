import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual, SelectMultiple
import sys
stdout = sys.stdout
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = stdout

data_file_path = "life_expectancy_data.csv"
dataframe = pd.read_csv(data_file_path)

draw_pair_cols = {
    'column_1': "Year",
    'column_2': "Life expectancy ",
    'country': "India"
}

drawable_cols = dataframe.drop(["Country", "Status"], axis=1).keys()

def draw_dataframe(df):
    df.plot(df.keys()[0], df.keys()[1:])
    plt.show()

def draw_pairs():
    countries = countryWidget.value
    if len(countries) == 0:
        return
    
    df = None
    
    for country in countries:
        filtered_frame = dataframe[dataframe['Country'] == country]
        filtered_frame = filtered_frame[[draw_pair_cols['column_1'], draw_pair_cols['column_2']]]
        filtered_frame.rename(columns={draw_pair_cols['column_2']: draw_pair_cols['column_2']+ '-' + country}, inplace = True)
        if df is None:
            df = filtered_frame
        else:
            df = pd.merge(df, filtered_frame, on='Year')

    df.plot(df.keys()[0], df.keys()[1:])
    plt.show()

def select_pair_column_1(column_1):
    if (column_1 == draw_pair_cols['column_2'] or column_1 == draw_pair_cols['column_1']):
        return
    draw_pair_cols['column_1'] = column_1
        
def select_pair_column_2(column_2="Life expectancy "):
    if (column_2 == draw_pair_cols['column_1'] or column_2 == draw_pair_cols['column_2']):
        return
    draw_pair_cols['column_2'] = column_2

def select_pair_country(country="India"):
    if (country == draw_pair_cols['country']):
        return
    draw_pair_cols['country'] = country

countryWidget = SelectMultiple(
    options=dataframe['Country'].unique(),
    value=['India', 'Iceland'],
    description='Country',
    disabled=False
)
