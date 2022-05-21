from operator import index
import pandas as pd
import openpyxl
df = pd.read_csv("CSV limpios/Candidaturas_2021_CLEAN.csv", header=0)
df_derivated = df[['ID REGION', 'REGION']]

df_without_duplicates = df_derivated.drop_duplicates()
df_without_duplicates.to_csv("Tablas_en_csv/Region.csv", index=False)

#print(df.head(5))