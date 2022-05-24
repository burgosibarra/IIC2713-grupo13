from operator import index
from pickle import TRUE
from sqlite3 import Timestamp
import pandas as pd
import numpy as np
import openpyxl
df_1 = pd.read_csv("CSV arreglados/Aportes_publicos_anual_arreglados_2.csv", header=0)
df_2 = pd.read_csv("CSV arreglados/Ingresos_Gastos_2017_Candidatos_CLEAN.csv", header=0)
df_3 = pd.read_csv("CSV arreglados/AAportes_Privados_2017_en_excel_2.csv", header=0)
df_derivated_1 = df_1[['Monto',	'Fecha de Pago']]
df_derivated_2 = df_2[['TIPO PLANILLA', 'FECHA DOCUMENTO', 'MONTO']]
df_derivated_3 = df_3[['Fecha de Transferencia', 'Monto']]


df_derivated_3['Fecha'] = df_derivated_3['Fecha de Transferencia']
df_derivated_1['Fecha'] = df_derivated_1['Fecha de Pago']
df_derivated_2['Fecha'] = df_derivated_2['FECHA DOCUMENTO']
df_derivated_2['Monto'] = df_derivated_2['MONTO']
df_derivated_2['Tipo'] = df_derivated_2['TIPO PLANILLA']



df_derivated_1['Tipo'] = np.where(df_derivated_1['Monto'] >= 0, 'INGRESO', 'nada')
df_derivated_3['Tipo'] = np.where(df_derivated_3['Monto'] >= 0, 'INGRESO', 'nada')



df_derivated_1 = df_derivated_1[['Tipo', 'Fecha', 'Monto']]
df_derivated_2 = df_derivated_2[['Tipo', 'Fecha', 'Monto']]
df_derivated_3 = df_derivated_3[['Tipo', 'Fecha', 'Monto']]




df_derivated_1['Fecha'] = df_derivated_1['Fecha'].apply(lambda x: x.split(' ')[0])
df_derivated_2['Fecha'] = df_derivated_2['Fecha'].str.replace("/", "-")



df_derivated = pd.concat([df_derivated_1, df_derivated_2, df_derivated_3])


'''
final = d1_derivate.merge(df_2, on=["TIPO DOCUMENTO"], how="left")


df_without_duplicates = df_derivated.drop_duplicates()
df_without_duplicates.to_csv("Region.csv", index=False)
'''
print(df_derivated.head(5))

''''
INGRESO/GASTO	
ID	int
Tipo	str
Candidatura.id	int
Aportantes.id	int
Fecha	date
Cuenta.id	int
monto	int

import pandas
import pandas as pd


def notas(nota):
    nota = int(nota.TheValue)
    if nota < 5:
        return 'Suspenso'
    elif nota < 9:
        return 'Aprobado'
    else:
        return 'Sobresaliente'


df = pd.DataFrame({'TheValue': ['4', '6', '9', '7'], 'Date':
                   ['02/20/2019', '01/15/2019', '08/21/2019', '02/02/2019']})
df['Date'] = pd.to_datetime(df.Date)
df['Result'] = df.apply(notas, axis=1)
dfsort = df.sort_values(by='Date')


'''