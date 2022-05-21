from operator import index
from pickle import TRUE
import pandas as pd
import openpyxl
df_1 = pd.read_csv("CSV limpios/Ingresos_Gastos_2017_Candidatos_CLEAN.csv", header=0)
df_derivated = df_1[['TIPO DOCUMENTO', 'DESCRIPCION TIPO DOCUMENTO']]
df_without_duplicates = df_derivated.drop_duplicates()


df_without_duplicates.to_csv("Tablas_en_csv/Tipo_documento.csv", index=False)


tupla = []
with open("Tablas_en_csv/Tipo_documento.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        tupla.append((line.split(",")[0], line.split(",")[1]))

with open("Tablas_en_csv/Tipo_documento.csv", "w") as document:
    print("ID,TIPO DOCUMENTO,DESCRIPCION TIPO DOCUMENTO", file=document)
    fila = 0
    for element in tupla:
        print(str(fila) + "," + element[0] + "," + element[1], file=document)
        fila += 1



#print(df_derivated.head(5))
