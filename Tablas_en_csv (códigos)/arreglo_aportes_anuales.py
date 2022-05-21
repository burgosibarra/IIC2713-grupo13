from operator import index
import pandas as pd
import openpyxl
df_1 = pd.read_csv("Aportes_publicos.csv", header=0)
df_1['ID'] = df_1.index
df_derivated_2 = df_1[['ID', 'PARTIDO_ID', 'Monto', 'Fecha de Pago', 'Trimestre']]
df_derivated_2.to_csv("Aportes_publicos.csv", index=False)

