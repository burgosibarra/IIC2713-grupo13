from codecs import ignore_errors
from ctypes.wintypes import INT
from operator import index
from pickle import TRUE
from sqlite3 import Timestamp
from tokenize import Ignore
import pandas as pd
import numpy as np
import openpyxl
df_2 = pd.read_csv("CSV limpios/Ingresos_Gastos_2017_Candidatos_CLEAN.csv", header=0)
df_derivated_2 = df_2[['TIPO PLANILLA', 'FECHA DOCUMENTO', 'MONTO', 'APORTANTEPROVEEDOR', 'DV', 'NOMBRE APORTANTEPROVEEDOR', 'TIPO CUENTA', 'NOMBRE PARTIDO', 'ID ELECCION', 'ID REGION', 'NOMBRE CANDIDATO']]
df_1 = pd.read_csv("Tablas_en_csv/Aportante.csv", header=0)
df_3 = pd.read_csv("Tablas_en_csv/Cuentas.csv", header=0)
df_4 = pd.read_csv("Tablas_en_csv/Candidatura.csv", header=0)
df_5 = pd.read_csv("Tablas_en_csv/Candidatos.csv", header=0)
df_6 = pd.read_csv("Tablas_en_csv/Partidos.csv", header=0)


df_1['APORTANTEPROVEEDOR'] = df_1['RUT']
df_3['ID_CUENTA'] = df_3['ID']
df_6['NOMBRE PARTIDO'] = df_6['NOMBRE']
df_5['NOMBRE CANDIDATO'] = df_5['NOMBRE']


df_derivated_2['CARGO'] = df_derivated_2['ID ELECCION']
'''
df_derivated_2['Monto'] = df_derivated_2['MONTO']
df_derivated_2['Tipo'] = df_derivated_2['TIPO PLANILLA']
'''


#df_derivated_2 = df_derivated_2[['Tipo', 'Fecha', 'Monto']]
df_derivated_2['FECHA DOCUMENTO'] = df_derivated_2['FECHA DOCUMENTO'].str.replace("/", "-")


final = df_derivated_2.merge(df_1, on=["APORTANTEPROVEEDOR", "DV"], how="left")
final['APORTANE_ID'] = final['ID']
final['ID_CUENTA'] = final['TIPO CUENTA']
final = final[['TIPO PLANILLA', 'FECHA DOCUMENTO', 'MONTO', 'APORTANE_ID', 'ID_CUENTA', "NOMBRE PARTIDO", 'CARGO','ID REGION', 'NOMBRE CANDIDATO']]
final_2 = final.merge(df_6, on=["NOMBRE PARTIDO"], how="left")
final_2['PARTIDO_ID'] = final_2['ID']
final_2 = final_2[['TIPO PLANILLA', 'FECHA DOCUMENTO', 'MONTO', 'APORTANE_ID', 'ID_CUENTA', 'CARGO', 'ID REGION', 'NOMBRE CANDIDATO']]
# esta super pero hay que elimianr la palabra partido del csv


# hacer merge con nombre candidato

final_3 = final_2.merge(df_5, on=['NOMBRE CANDIDATO'], how="left")
final_3['CANDIDATO_ID'] = final_3['ID']
final_3['CANDIDATO_ID'] = final_3['CANDIDATO_ID'].astype(int, errors='ignore')
final_3 = final_3[['TIPO PLANILLA', 'FECHA DOCUMENTO', 'MONTO', 'APORTANE_ID', 'ID_CUENTA', 'CARGO', 'ID REGION', 'CANDIDATO_ID']]



df_4['ID REGION'] = df_4['REGION.ID']
df_4['CANDIDATO_ID'] = df_4['CANDIDATO.ID']

final_4 = final_3.merge(df_4, on=['CARGO', 'ID REGION', 'CANDIDATO_ID'], how="left")
final_4['CANDIDATURA_ID'] = final_4['ID']
final_4 = final_4[['TIPO PLANILLA', 'FECHA DOCUMENTO', 'MONTO', 'APORTANE_ID', 'ID_CUENTA', 'CANDIDATURA_ID']]
# FALTA SOLO HACER MERGE CON LA CANDIDATURA PARA SABER EL ID PERO AUN NO ESTÁ LA CUSTIO
# LUEGO HABRÍA QUE HACER UN .PY ARREGLO PARA INDEXAR LOS INGRESOS GASTOS UWU Y SERÍA.
# antes falta hacer un merge con los partidos
# ID,*CARGO*,*REGION.ID*,TERRITORIO.ID,*CANDIDATO.ID*,ANO,*PARTIDO.ID*

'''
final = d1_derivate.merge(df_2, on=["TIPO DOCUMENTO"], how="left")


df_without_duplicates = df_derivated.drop_duplicates()
df_without_duplicates.to_csv("Region.csv", index=False)
'''
final_4.to_csv("IngresosGastos.csv", index=False)

print(final_4.head(125))

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