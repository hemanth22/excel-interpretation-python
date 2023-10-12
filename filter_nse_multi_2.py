import pandas as pd

df = pd.read_excel("MA-Equities-CM-volume-10-Oct-2023.xlsx", sheet_name="MA-Equities-CM-volume-10-Oct-20")

values_to_filter = ['SUZLON', 'IDEA', 'SOUTHBANK']

filtered_df = df[(df['SYMBOL \n'].isin(values_to_filter)) & (df['%CHNG \n'].astype(float) > -4 )]

print(filtered_df)

selected_columns = filtered_df[['SYMBOL \n', 'OPEN \n', 'HIGH \n', 'LOW \n', '%CHNG \n']]

print(selected_columns)

selected_columns.to_excel('filtered_symbol_data_cols.xlsx', index=False)
