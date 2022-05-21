from operator import index
import pandas as pd
import openpyxl
import re


df_1 = pd.read_csv("CSV limpios/Candidaturas_2013_2017_CLEAN.csv", header=0)
df_2 = pd.read_csv("CSV limpios/Candidaturas_2021_CLEAN.csv", header=0)
df_3 = pd.read_csv("CSV limpios/Aportes_Privados_2017_candidato_CLEAN.csv", header=0)
df_4 = pd.read_csv("CSV limpios/Total_afiliados_partidos_CLEAN2.csv", header=0)
df_5 = pd.read_csv("CSV limpios/Aportes_Privados_2017_partido_CLEAN.csv", header=0)
df_derivated_1 = df_1[['TERRITORIO']]
df_derivated_2 = df_2[['TERRITORIO']]
#df_3[['TERRITORIO']] = df_3[['Territorio']]
df_derivated_3 = df_3[['TERRITORIO']]
#df_5[['TERRITORIO']] = df_5[['Territorio']]
df_derivated_5 = df_5[['TERRITORIO']]
df_4[['TERRITORIO']] = df_4[['COMUNA']]
df_derivated_4 = df_4[['TERRITORIO']]
df_derivated = pd.concat([df_derivated_1, df_derivated_2, df_derivated_3, df_derivated_4, df_derivated_5])
data = df_derivated
df_without_duplicates = data.drop_duplicates()
df_without_duplicates = data.dropna()
#df_without_duplicates['ID'] = df_without_duplicates.index
#df_derivated_final = df_without_duplicates[['ID', 'TERRITORIO']]
df_derivated_final = df_without_duplicates[['TERRITORIO']]
df_derivated_final.to_csv("Tablas_en_csv/Territorio.csv", index=False)

#print(df_derivated.head(5))

distritos = set()
circunscripcion = set()
territorios = set()

with open("Tablas_en_csv/Territorio.csv", "r") as document:
    lines = document.readlines()
    fila = 0
    for line in lines[1::]:
        line = line.strip()
        if "DISTRITO" in line:
            number = re.sub(r'[^0-9]+', '', line)
            distritos.add("DISTRITO " + number)
        elif "CIRCUNSCRIPCION" in line:
            number = re.sub(r'[^0-9]+', '', line)
            circunscripcion.add("CIRCUNSCRIPCION " + number)
        else:
            territorios.add(line)

with open("Tablas_en_csv/Territorio.csv", "w") as document:
    fila = 0

    print("ID,TERRITORIO", file=document)

    circunscripcion_list = list(circunscripcion)
    circunscripcion_list.sort()
    for element in circunscripcion_list:
        print(str(fila) + "," + element, file=document)
        fila += 1

    distritos_list = list(distritos)
    distritos_list.sort()
    for element in distritos_list:
        print(str(fila) + "," + element, file=document)
        fila += 1
    
    territorios_list = list(territorios)
    territorios_list.sort()
    for element in territorios_list:
        print(str(fila) + "," + element, file=document)
        fila += 1
    
    print(str(fila) + "," + "INTERNACIONAL", file=document)