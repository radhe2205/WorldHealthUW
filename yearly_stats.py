import pandas as pd
import sys
from ipywidgets import interact, interactive, fixed, interact_manual, SelectMultiple
from IPython.display import display, HTML

data_file_path = "life_expectancy_data.csv"
dataframe = pd.read_csv(data_file_path)

metrics = dataframe.drop(["Country", "Status", 'Year'], axis=1).keys()

metricWidget = SelectMultiple(
    options=metrics,
    value=['Life expectancy '],
    description='Metrics: ',
    disabled=False
)

def show_year_wise_metrics():
    if len(metricWidget.value) == 0:
        return
    
    df = None
    
    for metric in metricWidget.value:
        filtered_frame = dataframe.sort_values(metric, ascending=False).drop_duplicates(['Year'])
        filtered_frame.sort_values('Year', ascending=True, inplace=True)
        filtered_frame = filtered_frame[['Year', 'Country']]
        filtered_frame.columns = ['Year', 'max-'+metric]

        if df is None:
            df = filtered_frame
        else:
            df = pd.merge(df, filtered_frame, on='Year')

        filtered_frame = dataframe.sort_values(metric, ascending=True).drop_duplicates(['Year'])
        filtered_frame.sort_values('Year', ascending=True, inplace=True)
        filtered_frame = filtered_frame[['Year', 'Country']]
        filtered_frame.columns = ['Year', 'min-'+metric]
        df = pd.merge(df, filtered_frame, on='Year')
    
    display(HTML(df.to_html()))

