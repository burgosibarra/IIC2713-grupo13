from operator import index
from pickle import TRUE
import pandas as pd
import openpyxl
df_1 = pd.read_csv("CSV arreglados/Ingresos_Gastos_2017_Candidatos_CLEAN.csv", header=0)
df_derivated = df_1[['TIPO DOCUMENTO', 'DESCRIPCION TIPO DOCUMENTO']]
df_without_duplicates = df_derivated.drop_duplicates()


df_without_duplicates.to_csv("Tipo_documento.csv", index=False)

print(df_derivated.head(5))
