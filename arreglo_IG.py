from operator import index
import pandas as pd
import openpyxl
df_1 = pd.read_csv("IngresosGastos.csv", header=0)
df_1['ID'] = df_1.index
df_derivated_2 = df_1[['ID', 'TIPO PLANILLA', 'FECHA DOCUMENTO', 'MONTO', 'APORTANE_ID', 'ID_CUENTA', 'CANDIDATURA_ID']]
df_derivated_2.to_csv("IngresosGastos.csv", index=False)

