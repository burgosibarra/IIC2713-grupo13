from operator import index
from pickle import TRUE
from sqlite3 import Timestamp
import pandas as pd
import numpy as np
import openpyxl
df_2 = pd.read_csv("CSV limpios/Ingresos_Gastos_2017_Candidatos_CLEAN.csv", header=0)
df_derivated_2 = df_2[['TIPO PLANILLA', 'FECHA DOCUMENTO', 'MONTO', 'APORTANTEPROVEEDOR', 'DV', 'NOMBRE APORTANTEPROVEEDOR', 'TIPO CUENTA']]
df_1 = pd.read_csv("Tablas_en_csv/Aportante.csv", header=0)
df_3 = pd.read_csv("Tablas_en_csv/Cuentas.csv", header=0)

df_3['ID_CUENTA'] = df_3['ID']

'''
df_derivated_2['Fecha'] = df_derivated_2['FECHA DOCUMENTO']

df_derivated_2['Monto'] = df_derivated_2['MONTO']
df_derivated_2['Tipo'] = df_derivated_2['TIPO PLANILLA']
'''


#df_derivated_2 = df_derivated_2[['Tipo', 'Fecha', 'Monto']]
df_derivated_2['FECHA DOCUMENTO'] = df_derivated_2['FECHA DOCUMENTO'].str.replace("/", "-")


final = df_derivated_2.merge(df_1, on=["APORTANTEPROVEEDOR", "DV"], how="left")
final['APORTANE_ID'] = final['ID']
final['ID_CUENTA'] = final['TIPO CUENTA']
final = final[['TIPO PLANILLA', 'FECHA DOCUMENTO', 'MONTO', 'APORTANE_ID', 'ID_CUENTA']]


# FALTA SOLO HACER MERGE CON LA CANDIDATURA PARA SABER EL ID PERO AUN NO ESTÁ LA CUSTIO
# LUEGO HABRÍA QUE HACER UN .PY ARREGLO PARA INDEXAR LOS INGRESOS GASTOS UWU Y SERÍA.



'''
final = d1_derivate.merge(df_2, on=["TIPO DOCUMENTO"], how="left")


df_without_duplicates = df_derivated.drop_duplicates()
df_without_duplicates.to_csv("Region.csv", index=False)
'''
print(final.head(5))

''''
INGRESO/GASTO	
ID	int
Tipo	str listo 
Candidatura.id	int
Aportantes.id	int listo 
Fecha	date listo 
Cuenta.id	int listo
monto	int listo 

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