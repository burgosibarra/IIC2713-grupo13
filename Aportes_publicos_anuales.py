from operator import index
import pandas as pd
import openpyxl
df_1 = pd.read_csv("CSV arreglados/Aportes_publicos_anual_arreglados_2.csv", header=0)
df_2 = pd.read_csv("Tablas_en_csv/Partidos.csv", header=0)

d1_derivate = df_1[['Nombre Partido', 'Monto', 'Fecha de Pago', 'Trimestre']]
d1_derivate["NOMBRE"] = d1_derivate['Nombre Partido']
final = d1_derivate.merge(df_2, on=["NOMBRE"], how="left")
final['PARTIDO_ID'] = final['ID']
final_2 = final[['PARTIDO_ID', 'Monto', 'Fecha de Pago', 'Trimestre']]
df_without_duplicates = final_2.drop_duplicates()
df_without_duplicates.to_csv("Aportes_publicos.csv", index=False)


'''
Aportes Publicos anuales	
Id	int
Partido.id	int
Monto 	int
Fecha	date
trimestre	str


'Nombre Partido', 'Monto', 'Fecha de Pago', 'Trimestre'

'''