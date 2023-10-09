import pandas as pd

df = pd.read_excel("user.xlsx")

filtered_df  = df[df['Age'] > 40 ]
print(filtered_df) 
