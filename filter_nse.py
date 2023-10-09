import pandas as pd

df = pd.read_excel("MA-Equities-CM-volume-10-Oct-2023.xlsx", sheet_name="MA-Equities-CM-volume-10-Oct-20")
print(df)

filtered_df  = df[df['%CHNG \n'].astype(float) > 5]
print(filtered_df)