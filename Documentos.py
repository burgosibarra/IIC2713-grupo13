from operator import index
import pandas as pd
import openpyxl
df_1 = pd.read_csv("CSV arreglados/Ingresos_Gastos_2017_Candidatos_CLEAN.csv", header=0)
df_2 = pd.read_csv("Tablas_en_csv/Tipo_documento.csv", header=0)

d1_derivate = df_1[['ID DOCUMENTO', 'TIPO DOCUMENTO','GLOSA DOCUMENTO']]
d1_derivate[['ID DOCUMENTO']] = d1_derivate[['ID DOCUMENTO']].astype(int)
final = d1_derivate.merge(df_2, on=["TIPO DOCUMENTO"], how="left")
final[['TIPO_DOCUMENTO_ID']] = final[['ID']]
final_2 = final[['ID DOCUMENTO', 'TIPO_DOCUMENTO_ID','GLOSA DOCUMENTO']]
df_without_duplicates = final_2.drop_duplicates()
df_without_duplicates.to_csv("Documentos.csv", index=False)


'''
Documentos	
ID	int
idarchivo	float
TipoDocumento.id	int
glosa	str
'''