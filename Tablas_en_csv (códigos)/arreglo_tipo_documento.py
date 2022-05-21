from operator import index
import pandas as pd
import openpyxl
df_1 = pd.read_csv("Tipo_documento.csv", header=0)
df_1['ID'] = df_1.index
df_derivated_2 = df_1[['ID', 'TIPO DOCUMENTO', 'DESCRIPCION TIPO DOCUMENTO']]
df_derivated_2.to_csv("Tipo_documento.csv", index=False)

