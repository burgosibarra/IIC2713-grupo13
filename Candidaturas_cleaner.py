import re
import pandas as pd

# "Candidaturas_2013_2017.csv"

output_document = open("Candidaturas_2013_2017_CLEAN.csv", "w")

with open('Candidaturas_2013_2017.csv', encoding="UTF-8", mode="r") as document:
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
        if (len(columns) > total_columnas):
            continue
        for i in range(0, len(columns)):
            columns[i] = ' '.join(columns[i].split())
            columns[i] = re.sub(r'[^A-Za-z0-9 ]+', '', columns[i])
        new_line = ';'.join(columns)
        print(new_line, file=output_document)
output_document.close()

df = pd.read_csv("Candidaturas_2013_2017_CLEAN.csv", header=0, sep=";")

df_without_duplicates = df.drop_duplicates()
# df_without_null = df_without_duplicates.dropna()
df_without_duplicates.to_csv("Candidaturas_2013_2017_CLEAN.csv", index=False)


# "Candidaturas_2021.csv"

output_document = open("Candidaturas_2021_CLEAN.csv", "w")
i = 0
with open("Candidaturas_2021.csv", encoding="UTF-8", mode="r") as document:
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
            index_rango = columns.index("RANGO")
        if (len(columns) != total_columnas):
            continue
        for i in range(0, len(columns)):
            columns[i] = ' '.join(columns[i].split())
            if (i != index_rango):
                columns[i] = re.sub(r'[^A-Za-z0-9 ]+', '', columns[i])
        if (columns[-2] == "MAPUCHE"):
            print(columns)
        if (columns[-1] != ""):
            new_line = ';'.join(columns)
            print(new_line, file=output_document)
output_document.close()

df = pd.read_csv("Candidaturas_2021_CLEAN.csv", header=0, sep=";")

df_without_duplicates = df.drop_duplicates()
#df_without_null = df_without_duplicates.dropna()
df_without_duplicates.to_csv("Candidaturas_2021_CLEAN.csv", index=False)
