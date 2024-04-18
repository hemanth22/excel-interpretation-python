import pandas as pd

df = pd.read_csv("MA-Equities-CM-volume-28-Oct-2023.csv")
#mask = ~df['SYMBOL \n'] #This is for field with na or NAN values
values_to_filter = ['SUZLON', 'IDEA', 'SOUTHBANK']

#filtered_df = df[mask & df['SYMBOL \n'].str.contains('|'.join(values_to_filter), na=False)] #This is for field with na or NAN values
filtered_df = df[df['SYMBOL \n'].str.contains('|'.join(values_to_filter))]
#print(filtered_df)

selected_columns = filtered_df[['SYMBOL \n', 'OPEN \n', 'HIGH \n', 'LOW \n', '%CHNG \n']]

print(selected_columns)

selected_columns.to_csv('filtered_symbol_data_cols.csv', index=False)
