import re
import pandas as pd

# "Ingresos_Gastos_2017_Candidatos_CLEAN.csv"

output_document_candidato = open("Aportes_Privados_2017_candidato_CLEAN.csv", "w")
output_document_partido = open("Aportes_Privados_2017_partido_CLEAN.csv", "w")

with open('Aportes_Privados_2017.csv', encoding="UTF-8", mode="r") as document:
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
            index_fecha = columns.index("FECHA DE TRANSFERENCIA")
        if (len(columns) != total_columnas):
            continue
        for i in range(0, len(columns)):
            if (i != index_fecha):
                columns[i] = re.sub(r'[^A-Za-z0-9 ]+', '', columns[i])
            columns[i] = ' '.join(columns[i].split())
        new_line = ';'.join(columns)
        if (columns[3] == "CANDIDATO"):
            print(new_line, file=output_document_candidato)
        elif (columns[3] == "PARTIDO"):
            print(new_line, file=output_document_partido)
        else:
            print(new_line, file=output_document_candidato)
            print(new_line, file=output_document_partido)


output_document_candidato.close()
output_document_partido.close()


df = pd.read_csv("Aportes_Privados_2017_candidato_CLEAN.csv", header=0, sep=";")

df_without_duplicates = df.drop_duplicates()
#df_without_null = df_without_duplicates.dropna()
df_without_duplicates.to_csv("Aportes_Privados_2017_candidato_CLEAN.csv", index=False)

df = pd.read_csv("Aportes_Privados_2017_partido_CLEAN.csv", header=0, sep=";")

df_without_duplicates = df.drop_duplicates()
#df_without_null = df_without_duplicates.dropna()
df_without_duplicates.to_csv("Aportes_Privados_2017_partido_CLEAN.csv", index=False)
