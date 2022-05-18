from operator import index
import pandas as pd
import openpyxl
df_1 = pd.read_csv("Candidatos.csv", header=0)
df_1['ID'] = df_1.index
df_derivated_2 = df_1[['ID', 'NOMBRE', 'SEXO', 'EDAD']]
df_derivated_2.to_csv("Candidatos.csv", index=False)

