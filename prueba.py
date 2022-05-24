from operator import index
from pickle import TRUE
import pandas as pd
import openpyxl
df_1 = pd.read_csv("CSV arreglados/Ingresos_Gastos_2017_Candidatos_CLEAN.csv", header=0)

df_1[['Nombre Aportante']] = df_1[['NOMBRE APORTANTEPROVEEDOR']]
df_derivated_1 = df_1[['APORTANTEPROVEEDOR', 'DV', 'Nombre Aportante']]
#df_without_duplicates = df_derivated_1.drop_duplicates('APORTANTEPROVEEDOR')


df_derivated_1.to_csv("Aportante_222.csv", index=False)

print(df_derivated_1.head(5))
