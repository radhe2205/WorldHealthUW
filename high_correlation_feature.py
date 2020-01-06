import pandas as pd
from IPython.display import display, HTML

data_file_path = "life_expectancy_data.csv"
dataframe = pd.read_csv(data_file_path)
metrics = dataframe.drop(["Country", "Status", 'Year'], axis=1).keys()

dataframe = dataframe[metrics]
pearson_corr = dataframe.corr(method='pearson')

df = pd.DataFrame(columns=['Feature', 'High correlation Feature', 'correlation value'])

for column in pearson_corr.columns:
    filtered_frame = pearson_corr[pearson_corr[column] <> 1]
    filtered_frame.loc[column] = abs(filtered_frame[column])
    filtered_frame = filtered_frame.sort_values(column, ascending=False)
    df = df.append(pd.DataFrame({'Feature': [column], 'High correlation Feature': [filtered_frame.index[0]], 'correlation value':[str(filtered_frame[column][0])]}), sort=False)

df = df.sort_values('correlation value', ascending=False)
