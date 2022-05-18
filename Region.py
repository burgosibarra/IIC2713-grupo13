from operator import index
import pandas as pd
import openpyxl
df = pd.read_csv("CSV arreglados/Candidaturas_2021_arreglado_2.csv", header=0)
df_derivated = df[['ID REGION', 'REGION']]

df_without_duplicates = df_derivated.drop_duplicates()
df_without_duplicates.to_csv("Region.csv", index=False)

print(df.head(5))