import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual, SelectMultiple
import numpy as np
import sys

stdout = sys.stdout
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = stdout

data_file_path = "life_expectancy_data.csv"
dataframe = pd.read_csv(data_file_path)
drawable_cols = dataframe.drop(["Country", "Status"], axis=1).keys()

featureWidget = SelectMultiple(
    options=drawable_cols,
    value=['Life expectancy '],
    description='Features',
    disabled=False
)

def draw_heatmap():
    filtered_frame = dataframe[np.asarray(featureWidget.value)]
    pearson_corr = filtered_frame.corr(method='pearson')

    sb.heatmap(pearson_corr, 
                xticklabels=pearson_corr.columns,
                yticklabels=pearson_corr.columns,
                cmap='RdBu_r',
                annot=True,
                linewidth=0.5)
