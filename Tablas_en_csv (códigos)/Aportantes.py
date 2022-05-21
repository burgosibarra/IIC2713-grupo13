from operator import index
from pickle import TRUE
import pandas as pd
import openpyxl
df_1 = pd.read_csv("CSV limpios/Ingresos_Gastos_2017_Candidatos_CLEAN.csv", header=0)
#df_2 = pd.read_csv("CSV limpios/AAportes_Privados_2017_en_excel_2.csv", header=0)

df_1[['Nombre Aportante']] = df_1[['NOMBRE APORTANTEPROVEEDOR']]
df_derivated_1 = df_1[['APORTANTEPROVEEDOR', 'DV', 'Nombre Aportante']]
#df_derivated_2 = df_2[['Nombre Aportante', 'Tipo Aportante', 'Tipo Aporte']]
#final = df_derivated_1.merge(df_derivated_2, on=["Nombre Aportante"], how="left")
#df_without_duplicates = final.drop_duplicates('APORTANTEPROVEEDOR')

df_without_duplicates = df_derivated_1.drop_duplicates()
df_without_duplicates.to_csv("Tablas_en_csv/Aportante.csv", index=False)

#print(df_without_duplicates.head(5))

with open("Tablas_en_csv/Aportante.csv", "r") as document:
    lines = document.readlines()

with open("Tablas_en_csv/Aportante.csv", "w") as document:
    fila = 0
    print("ID,RUT,DV,NOMBRE", file=document)
    for line in lines[1::]:
        line = line.strip().split(",")
        print(str(fila) + "," + str(int(float(line[0]))) + "," + line[1] + "," + line[2], file=document)
        fila += 1


