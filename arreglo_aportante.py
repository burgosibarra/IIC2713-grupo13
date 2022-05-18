from operator import index
import pandas as pd
import openpyxl
df_1 = pd.read_csv("Aportante.csv", header=0)
df_1['ID'] = df_1.index
df_derivated_2 = df_1[['ID', 'APORTANTEPROVEEDOR','DV','Nombre Aportante','Tipo Aportante','Tipo Aporte']]
df_derivated_2.to_csv("Aportante.csv", index=False)

