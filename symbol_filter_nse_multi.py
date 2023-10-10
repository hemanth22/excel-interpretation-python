import pandas as pd

df = pd.read_excel("MA-Equities-CM-volume-10-Oct-2023.xlsx", sheet_name="MA-Equities-CM-volume-10-Oct-20")

values_to_filter = ['SUZLON', 'IDEA', 'SOUTHBANK']

filtered_df = df[df['SYMBOL \n'].isin(values_to_filter)]
filtered_df.to_excel('filtered_symbol_data.xlsx', index=False)
