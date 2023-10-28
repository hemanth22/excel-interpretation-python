import pandas as pd

df = pd.read_csv("MA-Equities-CM-volume-28-Oct-2023.csv")

#print(df)

values_to_filter = ['SUZLON', 'IDEA', 'SOUTHBANK']

filtered_df = df[(df['SYMBOL \n'].isin(values_to_filter)) & (df['%CHNG \n'].astype(float) > 2 )]

#print(filtered_df)

selected_columns = filtered_df[['SYMBOL \n', 'OPEN \n', 'HIGH \n', 'LOW \n', '%CHNG \n']]

print(selected_columns)

selected_columns.to_csv('filtered_symbol_data_cols.csv', index=False)
