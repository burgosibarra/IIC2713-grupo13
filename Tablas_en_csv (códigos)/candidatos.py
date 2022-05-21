from operator import index
from pickle import TRUE
import pandas as pd
import openpyxl
df_1 = pd.read_csv("CSV limpios/Candidaturas_2013_2017_CLEAN.csv", header=0)
df_2 = pd.read_csv("CSV limpios/Candidaturas_2021_CLEAN.csv", header=0)
df_1[['NOMBRE']] = df_1[['CANDIDATO']]
df_2[['NOMBRE']] = df_2[['CANDIDATOA']]
df_derivated_1 = df_1[['NOMBRE', 'SEXO', 'EDAD']]
df_derivated_2 = df_2[['NOMBRE', 'SEXO', 'EDAD']]
df_derivated = pd.concat([df_derivated_1, df_derivated_2])
df_without_duplicates = df_derivated.drop_duplicates()
#df_without_duplicates[['EDAD']] = df_without_duplicates[['EDAD']].astype(int)
df_without_duplicates.to_csv("Tablas_en_csv/Candidatos.csv", index=False)

#print(df_derivated.head(5))