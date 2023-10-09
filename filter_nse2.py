import pandas as pd

df = pd.read_excel("MA-Equities-CM-volume-10-Oct-2023.xlsx", sheet_name="MA-Equities-CM-volume-10-Oct-20")
print(df)

filtered_df  = df[df['%CHNG \n'].astype(float) < 1]
print(filtered_df)

filtered_df.to_excel("filtered_excel.xlsx", index=False)

df = pd.read_excel("filtered_excel.xlsx")

selected_columns = ['SYMBOL \n', '%CHNG \n']
selected_df = df[selected_columns]


selected_df.to_excel("filtered_excel_cols.xlsx", index=False)
