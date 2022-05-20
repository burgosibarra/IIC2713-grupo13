import re
import pandas as pd

# "Ingresos_Gastos_2017_Candidatos_CLEAN.csv"

output_document = open("Ingresos_Gastos_2017_Candidatos_CLEAN.csv", "w")

with open('Ingresos_Gastos_2017_Candidatos.csv', encoding="UTF-8", mode="r") as document:
    lines = document.readlines()
    fila = 0
    for line in lines:
        line = line.strip()
        line = line.strip(";")
        line = line.upper()
        line = line.replace("Á", "A")
        line = line.replace("É", "E")
        line = line.replace("Í", "I")
        line = line.replace("Ó", "O")
        line = line.replace("Ú", "U")
        line = line.replace("Ý", "Y")
        line = line.replace("Ñ", "N")
        columns = line.split(";")
        if (fila == 0):
            total_columnas = len(columns)
            fila += 1
            index_fecha = columns.index("FECHA DOCUMENTO")
        if (len(columns) > total_columnas):
            continue
        for i in range(0, len(columns)):
            if (i != index_fecha):
                columns[i] = re.sub(r'[^A-Za-z0-9 ]+', '', columns[i])
            columns[i] = ' '.join(columns[i].split())
        new_line = ';'.join(columns)
        print(new_line, file=output_document)
output_document.close()

df = pd.read_csv("Ingresos_Gastos_2017_Candidatos_CLEAN.csv", header=0, sep=";")

df_without_duplicates = df.drop_duplicates()
df_without_null = df_without_duplicates.dropna()
df_without_null.to_csv("Ingresos_Gastos_2017_Candidatos_CLEAN.csv", index=False)


# "Total_afiliados_partidos_CLEAN.csv"

output_document = open("Total_afiliados_partidos_CLEAN.csv", "w")
i = 0
with open('Total_afiliados_partidos.csv', encoding="UTF-8", mode="r") as document:
    lines = document.readlines()
    fila = 0
    for line in lines:
        line = line.strip()
        line = line.strip(";")
        line = line.upper()
        line = line.replace("Á", "A")
        line = line.replace("É", "E")
        line = line.replace("Í", "I")
        line = line.replace("Ó", "O")
        line = line.replace("Ú", "U")
        line = line.replace("Ý", "Y")
        line = line.replace("Ñ", "N")
        columns = line.split(";")
        if (fila == 0):
            total_columnas = len(columns)
            fila += 1
            index_rango = columns.index("RANGO EDAD")
        if (len(columns) > total_columnas):
            continue
        for i in range(0, len(columns)):
            if (i != index_rango):
                columns[i] = re.sub(r'[^A-Za-z0-9 ]+', '', columns[i])
            columns[i] = ' '.join(columns[i].split())
        if (columns[2] == ""):
            columns[2] = "INTERNACIONAL"
        new_line = ';'.join(columns)
        print(new_line, file=output_document)
output_document.close()

df = pd.read_csv("Total_afiliados_partidos_CLEAN.csv", header=0, sep=";")

df_without_duplicates = df.drop_duplicates()
#df_without_null = df_without_duplicates.dropna()
df_without_duplicates.to_csv("Total_afiliados_partidos_CLEAN.csv", index=False)
