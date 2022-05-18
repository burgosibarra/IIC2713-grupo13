from operator import index
from pickle import TRUE
import pandas as pd
import openpyxl
df_1 = pd.read_csv("CSV arreglados/Candidaturas_2013_2017_arreglado_2.csv", header=0)
df_2 = pd.read_csv("CSV arreglados/Candidaturas_2021_arreglado_2.csv", header=0)
df_1[['NOMBRE']] = df_1[['CANDIDATO']]
df_derivated_1 = df_1[['NOMBRE', 'SEXO', 'EDAD']]
df_derivated_2 = df_2[['NOMBRE', 'SEXO', 'EDAD']]
df_derivated = pd.concat([df_derivated_1, df_derivated_2])
df_without_duplicates = df_derivated.drop_duplicates()
df_without_duplicates[['EDAD']] = df_without_duplicates[['EDAD']].astype(int)
df_without_duplicates.to_csv("Candidatos.csv", index=False)

print(df_derivated.head(5))