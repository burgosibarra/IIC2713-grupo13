from operator import index
import pandas as pd
import openpyxl
df_1 = pd.read_csv("Territorio.csv", header=0)
df_1['ID'] = df_1.index
df_derivated_final = df_1[['ID', 'TERRITORIO']]
df_derivated_final.to_csv("Territorio.csv", index=False)
