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

drawable_cols = dataframe.drop(["Country", "Status"], axis=1).keys()

pair_aggregate={
    "column_1": "Year",
    "column_2": "Life expectancy "
}

def select_aggregate_pair_1(column_1):
    if column_1 == pair_aggregate['column_1'] or column_1 == pair_aggregate['column_2']:
        return
    pair_aggregate["column_1"] = column_1
    
def select_aggregate_pair_2(column_2="Life expectancy "):
    if column_2 == pair_aggregate['column_1'] or column_2 == pair_aggregate['column_2']:
        return
    pair_aggregate["column_2"] = column_2

def draw_pair_aggregate(): 
    filtered_data = dataframe[[pair_aggregate['column_1'], pair_aggregate['column_2']]]
    
    filtered_data = filtered_data.groupby(pair_aggregate['column_1']).agg({pair_aggregate['column_2']: ['mean']}).reset_index()
    filtered_data.columns = filtered_data.columns.map('_'.join)
    
    filtered_data.plot(filtered_data.keys()[0], filtered_data.keys()[1:])
    plt.show()
